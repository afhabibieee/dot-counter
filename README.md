# dot-counter

## Project Domain
A program counts the number of dots on a domino built into a docker image run through a docker container.

## Problem Statements
- How do we get the contours of a given domino image?
- How to count the number of dots present in a given image?
- How to share the program's results so that others can access them?

## Solution Statements
- Get the threshold image from the input image that has been converted to grayscale based on threshing binary inverse and thresh otsu
- Searching the list of contours from the threshold image
- Get a list of contours for point drawings by input image type and calculate their total
- Display contour drawing
- Using streamlit as a container for web-based programs
- Create docker images and containers that run on-premises or in the cloud with Heroku and also store them on a docker hub

### Demo-example

##### single and multiple input images

<img src="https://drive.google.com/uc?export=view&id=1aV-2gfWaYaBvBOSNz0GW1hkXKnHWnSP-"
     alt="single image"
     style="float: left; margin-right: 100px;"
     width="100" />
<img src="https://drive.google.com/uc?export=view&id=16_RgnqYMl7foM51l1kD5eVMRUok4KpQx"
     alt="multiple images"
     style="float: left; margin-right: 10px;"
     width="300" />
     
##### outcomes

<img src="https://drive.google.com/uc?export=view&id=1Fr5BR2DnYaOegE3T24YBQIeHdltn3AZT"
     alt="single image"
     style="float: left; margin-right: 100px;"
     width="180" />
<img src="https://drive.google.com/uc?export=view&id=18XVUbH0WEEnYU3DHxY-HAtZ7riEbtnte"
     alt="multiple images"
     style="float: left; margin-right: 10px;"
     width="300" />
     
## How to Run This App via Docker
This image is available on Docker hub.
```
 https://hub.docker.com/repository/docker/afhabibieee/dotcounter
```
- Pull image: `docker pull afhabibieee/dotcounter:1.0`
- Run docker container: `docker run -p 8501:8501 afhabibieee/dotcounter:1.0`
- Go to : `localhost:8501`
