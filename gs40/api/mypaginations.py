from rest_framework import pagination
from rest_framework.pagination import CursorPagination

class Mypagination(pagination.CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = "cu"

