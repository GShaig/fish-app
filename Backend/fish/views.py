from rest_framework.response import Response
from rest_framework import permissions, views
from rest_framework.parsers import MultiPartParser, FormParser
from serializer import DataSerializer
from .models import Data
from rest_framework import status
import pandas as pd
from inference import model
import os, io, boto3
import seaborn as sns
import matplotlib.pyplot as plt

class DataUploadView(views.APIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.AllowAny]

    def get(self, request, format=None):
        dataset = Data.objects.all()
        serializer = DataSerializer(dataset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DataSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            csv_file = request.FILES['upload']
            csv_file.seek(0)
            df = pd.read_csv(csv_file, index_col=0)
            serializer.save()
            weights = model.predict(df)
            df['Weight'] = weights.tolist()
            sns.pairplot(df, kind='scatter', hue='Species')
            img_data = io.BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            s3_resource = boto3.resource('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                                         aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
            bucket = os.environ.get('S3_BUCKET')
            s3_resource.Object(bucket, 'data/plot.png').put(Body=img_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
