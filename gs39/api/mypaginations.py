from rest_framework import pagination
from rest_framework.pagination import LimitOffsetPagination

class Mypagination(pagination.LimitOffsetPagination):
    # pass
    default_limit = 5
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 10

