### Environment

The back-end server is developed with **Django REST Framework**.

You're supposed to have installed Django REST Framework before running the server. Please refer to [DRF Documention](https://www.django-rest-framework.org/tutorial/quickstart/) for details.

### Usage

Use `py manage.py runserver` to start the back-end server.

### API

- `/api/process_text`

Using method: `HTTP_POST`

Expected data format: `{'input_text': 'this is the data sent'}`

Return data format: `{'processed_text': 'this is the data returned'}`

Function: to uppercase 

- `/api/model_output`

Using method: `HTTP_POST`

Expected data format: `{'query': 'this is the data sent'}`

Return data format: `{'result': 'this is the data returned'}`

Function: to get the model output