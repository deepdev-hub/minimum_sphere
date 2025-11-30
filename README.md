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
