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

python init_shema.py
python itsajungleoutthere/app.py 

```

## Open question

I would use a matrix with all tags as columns.
For each line (= a photo), the detection or not of a cat, a dog and/or a bird is indicated by 1 or 0.
The 1 can also be replaced by the number of items detected.