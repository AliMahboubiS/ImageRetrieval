## ImageRetrieval

Implement a content-based image retrieval using Tensorflow and Numpy.

## Description

We rely on search engines like Google to retrieve the most relevant answers when we have queries. However, not all queries can be effectively answered through text-based searches.

For example, if you are trying to find a t-shirt online but do not know its name, you can describe it in text. But this approach might not yield the best results, as you will receive a wide variety of products that may not be similar to what you are searching for.

To address this issue, we can utilize the product's image by extracting its features and using those features to retrieve similar products. This concept is called content-based image retrieval.
## Dependencies

prerequisites, libraries, OS version, etc., needed before installing program.
```python
Tensorflow==2.11.0
Pillow==9.4.0
```

## Installing

first of all you should install requirments with code below:
```python
pip install -r requiremnets.txt
```
Executing program
for running the code you should use main.py file and run it.

```python
python main.py
```
## Data Set 

Caltech-UCSD Birds-200-2011 (CUB-200-2011)
Details
Caltech-UCSD Birds-200-2011 (CUB-200-2011) is an extended version of the CUB-200 dataset, with roughly double the number of images per class and new part location annotations.
Number of categories: 200
Number of images: 11,788
Annotations per image: 15 Part Locations, 312 Binary Attributes, 1 Bounding Box
For detailed information about the dataset, please see the technical report linked below.
https://www.vision.caltech.edu/datasets/cub_200_2011/

## Test sample and result base on similarity
![Crested_Auklet_0070_785261](https://user-images.githubusercontent.com/106017133/217498002-eabf10f4-c28f-4df0-84df-c1ff1b8d13c0.jpg)

result based on similarity distance

![image](https://user-images.githubusercontent.com/106017133/217498161-c957cd9b-7ddc-45ac-a30b-1fe85f357112.png)


## Authors

Contributors names and contact info

Ali Mahboubisarighieh mahboubi.ali1991@gmail.com

## Version History

0.1
Initial Release
## License

This project is licensed under the AliMahboubi License - see the LICENSE.md file for details
