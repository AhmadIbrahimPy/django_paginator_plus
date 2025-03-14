"""
📌 PaginatorHelper - Django Pagination Utility
=============================================

🚀 Developed by: Ahmad Ibrahim
🔗 LinkedIn: https://www.linkedin.com/in/ahmadibrahimpy/
🛠️ Built based on real-world experience to simplify pagination and data retrieval in Django projects.

🎯 Purpose:
This module provides an easy way to handle pagination in Django applications.
It efficiently splits large datasets into pages and returns structured responses with pagination details.

📜 Features:
✅ Splits data into pages based on the specified limit per page.
✅ Handles errors such as invalid page numbers or empty pages.
✅ Returns a clear message in case of any issue.
✅ Well-structured and clean code for easy integration into large projects.

🛠️ How to Use:
1️⃣ Instantiate `PaginatorHelper` with the list of items, `per_page` limit, and `page` number.
2️⃣ Call `get_data()` to retrieve the paginated result.

🔹 Example Usage:
---------------
items = ["Item1", "Item2", "Item3", ..., "Item1000.."]
paginator = PaginatorHelper(items, per_page=10, page=2)
result = paginator.get_data()
print(result)
# {'items': [...], 'page': 2, 'total_pages': 10, 'status_code': 200, 'msg': 'Pagination successful'}
"""


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from dataclasses import dataclass

@dataclass
class PaginatedResponse:
    """
    Data class to store paginated results along with status and message.
    """
    items: list
    page: int
    total_pages: int
    status_code: int
    msg: str


class PaginatorHelper:
    def __init__(self, items, per_page=10, page=1):
        """
        Constructor: Initializes pagination based on provided items.

        :param items: (List of items to paginate).
        :param per_page: (Number of items per page).
        :param page: (Page number to display).
        """
        self.response = PaginatedResponse([], 1, 0, 500, "Initialization error")
        self.per_page = per_page if isinstance(per_page, int) and per_page > 0 else 10
        self.page = page if isinstance(page, int) and page > 0 else 1

        try:
            self.paginator = Paginator(items, self.per_page)
            self.total_pages = self.paginator.num_pages

            if self.page > self.total_pages:
                self.page = self.total_pages  # ضبط رقم الصفحة ليكون ضمن النطاق

            self.current_page = self.paginator.page(self.page)
            self.response = PaginatedResponse(
                list(self.current_page),
                self.page,
                self.total_pages,
                200,
                "Pagination successful"
            )
        except PageNotAnInteger:
            self.response = PaginatedResponse([], 1, 0, 400, "Invalid page number format")
        except EmptyPage:
            self.response = PaginatedResponse([], 1, 0, 404, "Requested page is out of range")
        except Exception as e:
            self.response = PaginatedResponse([], 1, 0, 500, f"Error: {str(e)}")

    def get_data(self):
        """
        Returns structured paginated data after ensuring successful pagination.

        :return: `PaginatedResponse`
        """
        return self.response

    def __str__(self):
        return f"Page {self.page} of {self.total_pages}"

    def __repr__(self):
        return f"<PaginatorHelper page={self.page} total_pages={self.total_pages}>"
