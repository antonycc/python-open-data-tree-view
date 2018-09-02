# Purpose: Utility wrappers for persistence of suppporting data for Tree View

import sys
import datetime
from pathlib import Path

import config


logger = config.get_logger()


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
    if columns == None:
        columns = da.keys()
    logger.debug('head:')
    dump_dictarray_sub(da, columns, 0, 5)


def dump_dictarray_tail(da, columns=None):
    if columns == None:
        columns = da.keys()
    maxlen = dictarray_maxlen(da)
    logger.debug('tail:')
    dump_dictarray_sub(da, columns, max(0, maxlen - 5), maxlen)


def dump_dictarray_sub(da, columns, start, end):
    if columns == None:
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
