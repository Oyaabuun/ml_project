# ml_project

venv is not required in the docker
$PORTT IS ENV VARIABLE 

Build DOCKER IMAGE
docker build -t <image_name>:<tagname> . #docker build -t ml-project:latest .
note: imahe name for doceker must be lowercase

check the created docker images 
docker images 

RUN DOCKER IMAGE 
docker run -p 5000:5000 -e PORT=5000 a6ed2d709df3

Delete Docker Image:
Once you've identified the image you want to delete, you can use the docker rmi command followed by the image ID or image name. For example, if you want to delete an image with the ID image_id, you can use:

bash
Copy code
docker rmi -f image_id
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

#################################
To verify if the container is still present, you can use the docker ps -a command, which lists all containers, including stopped ones:

bash
Copy code
docker ps -a
If the container is listed, you can try stopping it again using either its ID or name. If it's not listed, it means the container has already been removed.

If you want to stop and remove all containers regardless of their status, you can use the following command:

bash
Copy code
docker stop $(docker ps -aq)
This command stops all running containers, and you can then remove them using:

bash
Copy code
docker rm $(docker ps -aq)