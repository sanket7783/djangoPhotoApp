# PhotoApp
This is a Django Rest framework backend for a photo gallery App. 
### Installation
+ Clone the repo
+ Do  `pip install -r requirements.txt` requirements file is present the project directory. \
 Note: *project is done on python3.5.x*

### Starting the App
+ Go inside django project dir and run following commands
1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py createsuperuser`
4. `python manage.py runserver`

Note: *Do make sure the application runs on 8000 or make the changes in the curl url ports accordingly in following endpoints*
### Following are the given features supported with corresponding curl commands.

1. JWT Authentication 
> curl --location --request POST 'http://127.0.0.1:8000/auth/token/'  --header 'Content-Type: application/json'  --data-raw '{
    "username":user_name,
    "password":passwprd
}'

2. post a photo
> curl --location --request POST 'http://localhost:8000/gallery/' \
--header 'Authorization: Bearer jwt_access_token_copied_from_jwt_requests_response' \
--form 'title="title_text"' \
--form 'caption="caption_text"' \
--form 'photo=@"/image/location/"' 

3. Save photo as draft
> curl --location --request POST 'http://localhost:8000/gallery/' \
--header 'Authorization: Bearer jwt_access_token_copied_from_jwt_requests_response' \
--form 'title="title_text"' \
--form 'caption="caption_text"' \
--form 'photo=@"/image/location/"' \
--form 'draft="true"'
4. Edit photo caption
> curl --location --request PATCH 'http://localhost:8000/gallery/photo/2/' \
--header 'Authorization: Bearer jwt_access_token_copied_from_jwt_requests_response' \
--form 'caption="caption_text1"'

5. Delete photos
> curl --location --request DELETE 'http://localhost:8000/gallery/photo/pk_id/' \
--header 'Authorization: Bearer jwt_access_token_copied_from_jwt_requests_response'

6. List photos \
>All photos 
>> curl --location --request GET 'http://localhost:8000/gallery/photo/list/' \
--header 'Authorization: Bearer jwt_access_token_copied_from_jwt_requests_response' 

>My photos
>> curl --location --request GET 'http://localhost:8000/gallery/photo/list?user=user_pk_id' \
--header 'Authorization: Bearer jwt_access_token_copied_from_jwt_requests_response'

>My drafts
>> curl --location --request GET 'http://localhost:8000/gallery/photo/list?user=user_pk_id&draft=true' \
--header 'Authorization: Bearer jwt_access_token_copied_from_jwt_requests_response'

7. Sort on publishing date
>ASC
>> curl --location --request GET 'http://localhost:8000/gallery/photo/list?ordering=publishing_date' \
--header 'Authorization: Bearer jwt_access_token_copied_from_jwt_requests_response'

>DESC
>> curl --location --request GET 'http://localhost:8000/gallery/photo/list?ordering=-publishing_date' \
8. Filter by user
> curl --location --request GET 'http://localhost:8000/gallery/photo/list?user=user_pk_id' \
--header 'Authorization: Bearer jwt_access_token_copied_from_jwt_requests_response'

9. photo size limit currently set to 1500kb size and 200X200 dimensions for the image.
