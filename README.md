# **PaginatorHelper - Django Pagination Utility**

## 🚀 Developed by: Ahmad Ibrahim

### **🔗 LinkedIn: [Ahmad Ibrahim](https://www.linkedin.com/in/ahmadibrahimpy/)**

**🛠️ Built based on real-world experience to simplify pagination and data retrieval in Django projects.**


# 🎯 Purpose

#### PaginatorHelper provides an easy way to handle pagination in Django applications.
#### It efficiently splits large datasets into pages and returns structured responses with pagination details.

# 📜 Features

#### ✅ Splits data into pages based on the specified limit per page.
#### ✅ Handles errors such as invalid page numbers or empty pages.
#### ✅ Returns a clear message in case of any issue.
#### ✅ Well-structured and clean code for easy integration into large projects.

## 📌 Installation

#### PaginatorHelper requires Django 4.2 or later to work properly.
#### Ensure that Django is installed in your environment before using this package:

`# pip install django>=4.2`

## 🛠️ How to Use

#### 1️⃣ Instantiate PaginatorHelper with the list of items, per_page limit, and page number.
#### 2️⃣ Call get_data() to retrieve the paginated result.

## 🔹 Example Usage

`from paginator_helper import PaginatorHelper

items = ["Item1", "Item2", "Item3", ..., "Item1000"]  # Example dataset
paginator = PaginatorHelper(items, per_page=10, page=2)
result = paginator.get_data()

print(result)
Output:
{
   'items': [...],
   'page': 2,
   'total_pages': 10,
   'status_code': 200,
   'msg': 'Pagination successful'
}`

## 🔄 Response Structure
#### The get_data() method returns a structured response:

`{
  "items": [...],  # List of paginated items
  "page": 2,  # Current page number
  "total_pages": 10,  # Total number of pages
  "status_code": 200,  # HTTP-like status code
  "msg": "Pagination successful"  # Status message
}`

## 📜 Error Handling
* ### 1 Error Type : Invalid Page Format
  * #### Status Code: 400
  * #### Message: "Invalid page number format"
* ### 2 Error Type : Page Out of Range
  * #### Status Code: 404
  * #### Message: "Requested page is out of range"
* ### 3 Error Type : Unexpected Error
  * #### Status Code: 500
  * #### Message: "Error: [Exception Message]"

## 🔧 Contributing

### Feel free to contribute, report issues, or suggest improvements! 😊

### Made with ❤️ by [Ahmad Ibrahim](https://www.linkedin.com/in/ahmadibrahimpy/).