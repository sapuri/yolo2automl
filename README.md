# YOLO2AutoML
Convert a YOLO file to AutoML format for Cloud AutoML Vision Object Detection.

## Usage

```
usage: convert.py [-h] [-o OUTPUT] yolo_filepath automl_filepath label

YOLO2AutoML: Convert a YOLO format file to AutoML format for Cloud AutoML
Vision Object Detection.

positional arguments:
  yolo_filepath         Input your YOLO format file path. (e.g. yolo.txt)
  automl_filepath       Input your AutoML exported file path. (e.g.
                        export.csv)
  label                 Input the label name. (e.g. car)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Input the output file name. (default: output.csv)
```
