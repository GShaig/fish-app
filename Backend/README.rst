=====
Fish Backend API
=====

Fish Backend API is a Django app serving as a backend API for Fish app. The API takes a CSV file as an input, turns it into a Pandas dataframe and uses a special model to predict fish weights based on their dimensions. After necessary calculations, the app adds 'Weight' column to the dataframe and visualizes the results on a seaborn graph.

1. Add "fish" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'fish.apps.FishConfig',
    ]

2. Include the fish URLconf in your project urls.py like this::

    path('', include('fish.urls')),

3. Run ``python manage.py migrate`` to create the fish models.

4. Start the development server and visit http://localhost:8000/admin/
   for the admin panel.