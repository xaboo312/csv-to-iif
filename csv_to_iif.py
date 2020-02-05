import csv


def get_headers(filename, newline_arg='', encoding_arg='ascii', delimiter_arg='\t'):
    """gets the headers from a csv/iif file and returns them"""
    header_file = open(filename, newline=newline_arg, encoding=encoding_arg)
    header_dict_reader = csv.DictReader(header_file, delimiter=delimiter_arg)
    return header_dict_reader.fieldnames


def get_row(filename, row_num, newline_arg='', encoding_arg='ascii', delimiter_arg='\t'):
    """gets a row from a csv/iif file and returns it as OrderedDict"""
    row_file = open(filename, newline=newline_arg, encoding=encoding_arg)
    row_dict_reader = csv.DictReader(row_file, delimiter=delimiter_arg)
    row_list = list(row_dict_reader)
    return row_list[row_num]


def modify_row(iif_writer, row_list, header, value):
    """changes the value in a row using a header s a key"""
    row_list[header] = value
    iif_writer.writerow(row_list)
    return row_list


def write_headers(filename, headers, newline_arg='', encoding_arg='ascii', delimiter_arg='\t'):
    new_iif = open(filename, 'w', newline=newline_arg, encoding=encoding_arg)
    iif_writer = csv.DictWriter(new_iif, headers, delimiter_arg)
    iif_writer.writeheader()
    return iif_writer


if __name__ == '__main__':
    print(get_headers('ITEM-AND-INVOICE-TEMPLATE.iif'))
