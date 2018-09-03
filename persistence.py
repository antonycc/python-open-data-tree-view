# Purpose: Utility wrappers for persistence of suppporting data for Tree View

import hashlib

import config

# Config
logger = config.get_logger()
allowed_extensions = set(['csv'])


def to_logging(df, floor_height_column, face_direction_column, window_vertical_position_column):
    da = to_dictarray(df, {floor_height_column: [], face_direction_column: [], window_vertical_position_column: []})
    dump_dictarray_head(da)
    dump_dictarray_tail(da)


def to_dictarray(df, da):
    for df_row in df.itertuples():
        dfdict_row = df_row._asdict()
        dr = {}
        for column in da.keys():
            try:
                da[column].append(float(dfdict_row[column]))
            except Exception as e:
                da[column].append(dfdict_row[column])
    return da


def dump_dictarray_head(da, columns=None):
    if not columns:
        columns = da.keys()
    logger.debug('head:')
    dump_dictarray_sub(da, columns, 0, 5)


def dump_dictarray_tail(da, columns=None):
    if not columns:
        columns = da.keys()
    maxlen = dictarray_maxlen(da)
    logger.debug('tail:')
    dump_dictarray_sub(da, columns, max(0, maxlen - 5), maxlen)


def dump_dictarray_sub(da, columns, start, end):
    if not columns:
        columns = da.keys()
    for i in range(start, end):
        row_str = '('
        for column in columns:
            if i < len(da[column]):
                row_str = '{} {}'.format(row_str, da[column][i])
            else:
                row_str = '{} --'.format(row_str)
        logger.debug('[{}]: {} )'.format(i, row_str))


def dictarray_maxlen(da):
    columns = da.keys()
    maxlen = 0
    for column in columns:
        maxlen = max(maxlen, len(da[column]))
    return maxlen


def populated_file(request, parameter_name):
    return parameter_name in request.files \
           and request.files[parameter_name] \
           and request.files[parameter_name].filename


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


def sha3(b):
    return hashlib.sha3_256(b.encode('utf-8')).hexdigest()
