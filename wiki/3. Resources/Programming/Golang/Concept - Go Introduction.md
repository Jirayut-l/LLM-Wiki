---
tags: [golang, introduction, basic]
---

# Concept - Go Introduction (บทนำสู่ภาษา Go)

บทนำเบื้องต้นเกี่ยวกับภาษา Go (หรือ Golang) ออกแบบมาเพื่อผู้เริ่มต้น โดยครอบคลุมตั้งแต่โครงสร้างพื้นฐานไปจนถึงการควบคุมทิศทางของโปรแกรม.

## ภาษา Go คืออะไร?
Go เป็นภาษาโปรแกรมที่พัฒนาโดย Google เน้นความเรียบง่าย (Simplicity), ประสิทธิภาพ (Performance), และการทำงานร่วมกันอย่างมีประสิทธิภาพ (Concurrency). Go ถูกสร้างมาเพื่อแก้ปัญหาความซับซ้อนในระบบขนาดใหญ่ (Cloud Native, Microservices).

## โครงสร้างพื้นฐานของโปรแกรม Go
ทุกไฟล์ในภาษา Go ต้องประกอบด้วย 3 ส่วนหลักเสมอ:

1.  **Package Declaration**: บรรทัดแรกต้องบอกว่าไฟล์นี้อยู่ใน package อะไร. หากเป็นโปรแกรมที่สามารถรันได้ (Executable) ต้องใช้ชื่อ `package main`.
2.  **Import**: การนำเข้า package อื่นๆ มาใช้งาน เช่น `fmt` (Format) สำหรับการพิมพ์ข้อความ.
3.  **Function main()**: ฟังก์ชันหลักที่เป็นจุดเริ่มต้นของโปรแกรม.

### ตัวอย่างโค้ด: Hello World และคำอธิบาย
```go
package main // 1. ชื่อ package

import "fmt" // 2. นำเข้า library มาตรฐาน

func main() { // 3. จุดเริ่มต้นการทำงาน
    fmt.Println("สวัสดี Go! ยินดีต้อนรับสู่โลกของ Gopher")
}
```

## การประกาศตัวแปรและค่าคงที่ (Variables & Constants)
Go มีความเข้มงวดเรื่องประเภทข้อมูล (Strongly Typed) แต่ก็มี syntax ที่ช่วยให้เขียนได้สั้นลง.

```go
package main

import "fmt"

func main() {
    // 1. ประกาศแบบเต็ม (ระบุ Type)
    var name string = "Alice"
    
    // 2. ประกาศแบบสั้น (Short Declaration) - นิยมใช้ในฟังก์ชัน
    age := 30 // Go จะรู้เองว่าเป็น int
    
    // 3. ประกาศค่าคงที่ (เปลี่ยนค่าไม่ได้)
    const Pi = 3.14
    
    fmt.Printf("ชื่อ: %s, อายุ: %d, ค่า Pi: %.2f\n", name, age, Pi)
}
```

## การควบคุมทิศทางของโปรแกรม (Control Structures)

### 1. If-Else (การตัดสินใจ)
ใน Go เราไม่ต้องใส่เครื่องหมาย `()` รอบเงื่อนไข.
```go
score := 85
if score >= 80 {
    fmt.Println("คุณได้เกรด A")
} else if score >= 70 {
    fmt.Println("คุณได้เกรด B")
} else {
    fmt.Println("พยายามต่อไป!")
}
```

### 2. For Loop (การวนซ้ำ)
Go มีคำสั่งวนซ้ำเพียงแบบเดียวคือ `for` แต่สามารถประยุกต์ใช้ได้หลายแบบ.
```go
// แบบมาตรฐาน
for i := 0; i < 5; i++ {
    fmt.Println("รอบที่:", i)
}

// แบบ While Loop (ใช้ for แทน)
n := 1
for n < 5 {
    fmt.Println("n =", n)
    n++
}
```

## ฟังก์ชัน (Functions)
ฟังก์ชันช่วยให้เราแบ่งโค้ดเป็นส่วนย่อยๆ เพื่อนำกลับมาใช้ใหม่ได้ง่าย.
```go
func add(a int, b int) int {
    return a + b
}

// เรียกใช้งานใน main
result := add(10, 20)
fmt.Println("ผลบวก:", result)
```

## การรันโปรแกรม (Running Go Code)
ใช้คำสั่งผ่าน Terminal หรือ Command Prompt:
-   **Run ทันที**: `go run filename.go`
-   **Build เป็นไฟล์ .exe (Windows)**: `go build filename.go`

## จุดเด่นสำหรับมือใหม่
-   **ไม่มี Semicolon**: ไม่ต้องใส่ `;` ท้ายบรรทัด (Go จะใส่ให้เองเบื้องหลัง).
-   **Fast Compilation**: คอมไพล์เร็วมาก ไม่ต้องรอนาน.
-   **Zero Value**: ตัวแปรที่ประกาศแล้วยังไม่ใส่ค่า จะมีค่าเริ่มต้นเสมอ (เช่น `int` เป็น `0`, `string` เป็น `""`).

## แหล่งอ้างอิงและลิงก์ที่เกี่ยวข้อง
- [[Concept - Go Data Types]]
- [[Summary - Mastering Go 4th Edition]]
