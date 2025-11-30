# Grey Wolf Optimization (GWO) – Tối thiểu hóa hàm Sphere

## 1.  Thông tin nhóm

**Nhóm 151**, gồm các sinh viên thực hiện:

| STT | Họ và tên        | MSSV     |
|----|------------------|----------|
| 1  | Lương Văn Hưng   | 20235740 |
| 2  | Phạm Thế Đạt      | 20235776 |

---

## 2.  Giới thiệu

Dự án này triển khai **thuật toán Grey Wolf Optimization (GWO)** để giải bài toán tối ưu hàm Sphere – một trong những hàm benchmark phổ biến để đánh giá thuật toán tối ưu meta-heuristic.

GWO mô phỏng hành vi:
- phân cấp bầy sói (α, β, δ, ω),
- bao vây con mồi,
- tấn công con mồi,
- tìm kiếm – khai thác không gian nghiệm.

Mục tiêu của bài toán là tìm nghiệm \( x \) sao cho:

\[
f(x) = \sum_{i=1}^{n} x_i^2
\]

đạt giá trị nhỏ nhất.

---

## 3.  Cài đặt & Thiết lập môi trường

###  Yêu cầu môi trường
- Python **3.8+**
- Bộ thư viện:
  - `numpy`
  - `matplotlib`

###  Cài đặt thư viện
Chạy lệnh:

```bash
pip install numpy matplotlib

```
###  Cấu trúc file
 GWO-Sphere-Optimization
 ├── minimum_of_sphere.py   # Code thuật toán GWO + vẽ biểu đồ hội tụ
 └── README.md

###  Chạy chương trình

Trong terminal:

```bash
python minimum_of_sphere.py
```

---

## 4.  Mô tả chi tiết

File `minimum_of_sphere.py` gồm các thành phần chính:

###  Hàm mục tiêu (Objective Function)

* Sphere function
* Liên tục, lồi, đơn giản, dùng để test thuật toán tối ưu

###  Thuật toán Grey Wolf Optimization

Gồm các bước:

1. Khởi tạo đàn sói ngẫu nhiên
2. Xác định 3 con sói tốt nhất:

   * **Alpha (α)** – nghiệm tốt nhất
   * **Beta (β)** – nghiệm tốt thứ hai
   * **Delta (δ)** – nghiệm tốt thứ ba
3. Cập nhật vị trí theo mô hình bao vây & săn mồi
4. Lặp lại qua nhiều vòng để hội tụ nghiệm tối ưu

###  Biểu đồ hội tụ

* Sử dụng matplotlib để hiển thị tiến trình giảm của:

  * Best fitness value (Alpha score)
  * Qua từng iteration

---

## 5.  Kết quả

Khi chạy chương trình:

* Thuật toán hội tụ rất nhanh về nghiệm gần **(0, 0, 0, …)**
* Kết quả in ra:

  * **Best Score** (giá trị nhỏ nhất của hàm Sphere)
  * **Best Position** (vector nghiệm tốt nhất)
* Một **biểu đồ hội tụ (Convergence Curve)** được hiển thị, minh họa quá trình thuật toán tiến dần về cực tiểu.

Ví dụ:

```
Best Score: 0.00000021
Best Position: [ 0.0021 -0.0010  0.0008 ... ]
```

---

## 6.  Hỗ trợ – Liên hệ

Nếu bạn có thắc mắc hoặc cần hỗ trợ thêm, vui lòng liên hệ:

**Email:** [hung.lv235740@sis.hust.edu.vn](mailto:hung.lv235740@sis.hust.edu.vn)

