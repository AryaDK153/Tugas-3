## Link Herokuapp

[HTML view](https://fistofadventure.herokuapp.com/mywatchlist/html/)

[XML view](https://fistofadventure.herokuapp.com/mywatchlist/xml/)

[JSON view](https://fistofadventure.herokuapp.com/mywatchlist/json/)


## Perbedaan JSON, XML, dan HTML

HTML berisi format untuk tampilan, sedangkan XML dan JSON berisi data yang ingin ditampilkan.

Format XML dan JSON membutuhkan CSS atau Javascript agar dapat muncul di tampilan browser, sedangkan format html bisa langsung muncul di tampilan browser.

File XML lebih besar dari JSON karena format penulisannya. 


## Mengapa data delivery dibutuhkan dalam pengimplementasian sebuah platform?

Data delivery dilakukan agar browser dapat menerima respon dari server sesuai request yang diminta. Misalnya, ketika browser meminta laman HTML, server akan mengembalikan file HTML yang sudah diformat selama pembuatan web. Selain itu, browser juga dapat meminta data dalam bentuk yang diinginkan, misalnya, browser meminta data dalam bentuk JSON, maka server akan mengembalikan data dalam bentuk JSON. 


## Pengimplementasian Tugas-3 : Poin 1-3

1. Buka command prompt, masukkan "python manage.py startapp mywatchlist", tambahkan INSTALLED_APPS di settings.py.

2. Masuk ke folder app yang telah dibuat, buat file baru bernama urls.py, import "path" yang disediakan django untuk membuat path, serta fungsi-fungsi dalam views.py yang akan dibuat, buat list urlpatterns yang akan diakses. Jangan lupa untuk menambahkan urlpattern menuju app yang telah dibuat di project_django/urls.py

3. Buka models.py kemudian buat fungsi dengan parameter models yang dapat diimport dari django, buat variabel-variabel untuk model yang diinginkan, pastikan masing-masing memiliki data-type yang benar, model yang telah dibuat akan dapat dibaca oleh views.py setelah melakukan migration dengan 'python manage.py makemigration', jika belum memiliki folder migration, dan 'python manage.py migrate'. Ini perlu dilakukan agar django dapat mendeteksi perubahan pada models.py.


## Postman URL test
# HTML
https://user-images.githubusercontent.com/112199564/191650400-6eb4d4e1-64cc-446b-a3fa-ccafa0216114.png

# XML
https://user-images.githubusercontent.com/112199564/191651653-f73a821d-5f7c-4144-a144-258ce0a8eb87.png

# JSON
https://user-images.githubusercontent.com/112199564/191651947-34e8113f-1728-47f6-b9a8-502019cd45e8.png