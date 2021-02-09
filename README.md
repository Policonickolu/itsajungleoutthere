# itsajungleoutthere

A simple web API to help a Machine Learning team organize its data. The
data consist of image that have tags, those tags are the labeling of the image. For
exemple an image can be labeled with "Dog" if there is a dog in the image.


## Context

I never used Flask before but I didn't do the test in node, I found some tutorial and examples.
I tried to do the bonus with dataset and label, before removing them.

## User Stories:
1. AADS (As a Data Scientist) I can upload an image, it stores a url, a name, a
type.
2. AADS I can paginate on all the image I have uploaded
3. AADS I can create new Tags, the tags only have a name. For exemple a tag
"Cat")
4. AADS I can list all of the existing Tags
5. AADS I can add a tag to an image to signify that this image has the tag "Cat"
6. AADS I can list all the tags of an image.
7. AADS I can paginate all the images that have a tag.


## How to run


```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python setup.py develop
python init_shema.py
python itsajungleoutthere/app.py 

```

the page ```http://localhost:8888/api/``` should open with a detailed Swagger page with all available queries from the REST API.

```
GET		/images/							get all images with pagination
POST	/images/							upload image
GET		/images/:id 						get image from id
DELETE	/images/:id 						delete image from id
PUT 	/images/:id 						modify image from id
GET 	/images/:image_id/tags 				get all tags of the image from image_id
PUT 	/images/:image_id/tags/:tag_id 		add tag tag_id to the image image_id

GET		/tags/								get all tags with pagination
POST	/tags/								upload tag
GET		/tags/:id 							get tag from id
DELETE	/tags/:id 							delete tag from id
PUT 	/tags/:id 							modify tag from id
GET 	/tags/:tag_id/images 				get all images with the tag tag_id with pagination
```

A REST API uri have to be resources oriented, and not actions oriented. that's why there is no key word as "all" or "add" or "new"

## Open question

I would use a matrix with all tags as columns.
For each line (= a photo), the detection or not of a cat, a dog and/or a bird is indicated by 1 or 0.
The 1 can also be replaced by the number of items detected.