**(a)Actor/role:** admin, operator, viewer. 
- Muc dich goi ham la de tra cuu thong tin chi tiet tu du lieu JSON do API giam sat ha tang mang tra ve.

**(b)Asset nhay cam:** apiKey (khoa xac thuc), managementIpAddress (IP quan tri).

**(c)Trust boundary:** ranh gioi phan quyen se bi bo qua neu ham `json_search()` tra cuu va tra ve ket qua truc tiep ma khong kiem tra xem user goi ham co mang `role` hop le khong

**(d)Threat (STRIDE):** moi de doa nay thuoc nhom *information Disclosure*. Mot user chi co quyen *viewer* lai co the truyen vao tu khoa tim kiem la *apiKey* va xem duoc khoa xac thuc bi mat cua he thong. 
        