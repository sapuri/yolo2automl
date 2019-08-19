import argparse
import csv


def main():
    parser = argparse.ArgumentParser(description='YOLO2AutoML: Convert a YOLO file to AutoML format.')
    parser.add_argument('yolo_filepath', help='Input a YOLO file path. (e.g. yolo.txt)')
    parser.add_argument('automl_filepath', help='Input an AutoML exported file path. (e.g. export.csv)')
    parser.add_argument('-o', '--output', default='output.csv',
                        help='Input the output file name. (default: output.csv)')

    args = parser.parse_args()
    yoro_filepath = args.yolo_filepath
    automl_filepath = args.automl_filepath
    output_filename = args.output

    yoro_lines = []
    with open(yoro_filepath) as f:
        for line in f:
            yoro_lines.append(convert(line.rstrip('\n')))

    automl_lines = []
    with open(automl_filepath) as f:
        for line in f:
            automl_lines.append(line.rstrip('\n'))

    if len(yoro_lines) != len(automl_lines):
        print('The two input files must have the same number of lines.')
        exit(1)

    output_lines = []
    for i, line in enumerate(yoro_lines):
        spl = automl_lines[i].split(',')
        output_line = [spl[0], spl[1], spl[2]]
        for j, value in enumerate(line.split(',')):
            output_line.append(value)
        output_lines.append(output_line)

    try:
        export2csv(output_lines, output_filename)
    except BaseException as e:
        print('failed to export to csv:', e)
        exit(1)

    print('Saved:', output_filename)


def convert(line: str) -> str:
    # YOLO format: 1 0.365234 0.541016 0.386719 0.847656
    # AutoML format: TRAIN,gs://cloud-ml-data/img/openimage/2851/11476419305_7b73a0128c_o.jpg,Baked goods,0.56,0.25,0.97,0.25,0.97,0.50,0.56,0.50

    _, x1, y1, x2, y2 = line.split(' ')
    x1 = round(float(x1), 2)
    y1 = round(float(y1), 2)
    x2 = round(float(x2), 2)
    y2 = round(float(y2), 2)
    return f'{x1},{y1},{x2},{y1},{x2},{y2},{x1},{y2}'


def export2csv(output_lines: list, filename: str):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(output_lines)


if __name__ == '__main__':
    main()
