from django.db import models

# import os
# import random
# import string


# def random_file_name(instance, filename):
#     # Get extension
#     ext = filename.split('.')[-1]
#     # Generate random 10 characters
#     random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
#     # New filename
#     filename = f"{random_str}.{ext}"
#     return os.path.join("excel_files", filename)

# class ExcelFile(models.Model):
#     file = models.FileField(upload_to=random_file_name)

#     def __str__(self):
#         return str(self.file)

