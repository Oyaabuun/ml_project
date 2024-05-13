# ml_project

venv is not required in the docker
$PORTT IS ENV VARIABLE 

Build DOCKER IMAGE
docker build -t <image_name>:<tagname> . #docker build -t ml-project:latest .
note: imahe name for doceker must be lowercase

check the created docker images 
docker images 

RUN DOCKER IMAGE 
docker run -p 5000:5000 -e PORT=5000 7d5fd91d1a76

Delete Docker Image:
Once you've identified the image you want to delete, you can use the docker rmi command followed by the image ID or image name. For example, if you want to delete an image with the ID image_id, you can use:

bash
Copy code
docker rmi image_id
If you prefer to delete the image by its name and tag, you can use:

bash
Copy code
docker rmi image_name:tag
Replace image_id with the actual ID of the image you want to delete, and image_name:tag with the name and tag of the image you want to delete.

Delete Multiple Images:
You can also delete multiple images at once by specifying their IDs or names separated by spaces. For example:

bash
Copy code
docker rmi image_id1 image_id2 image_id3

or

bash
Copy code
docker rmi image_name1:tag1 image_name2:tag2 image_name3:tag3

Replace image_id1, image_id2, etc., with the actual IDs of the images you want to delete, or replace image_name1:tag1, image_name2:tag2, etc., with the actual names and tags of the images you want to delete.