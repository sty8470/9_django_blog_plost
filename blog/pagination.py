from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'total_count': self.page.paginator.count,
            'count': len(data),
            'prev_page': self.get_previous_link(),
            'next_page': self.get_next_link(),
            'results': data
        })
