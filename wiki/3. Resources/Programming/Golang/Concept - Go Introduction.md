---
tags: [golang, introduction, basic]
---

# Concept - Go Introduction (บทนำสู่ภาษา Go)

บทนำเบื้องต้นเกี่ยวกับภาษา Go (หรือ Golang) โดยอ้างอิงเนื้อหาพื้นฐานจาก Chapter 1 ของ [[Summary - Mastering Go 4th Edition]].

## ภาษา Go คืออะไร?
Go เป็นภาษาโปรแกรมที่พัฒนาโดย Google เน้นความเรียบง่าย (Simplicity), ประสิทธิภาพ (Efficiency), และรองรับการทำงานแบบขนาน (Concurrency) ได้ดีเยี่ยม

## โครงสร้างพื้นฐานของโปรแกรม Go
โปรแกรม Go จะประกอบด้วย:
1. **Package Declaration**: ทุกไฟล์ต้องระบุว่าอยู่ใน package ไหน (ไฟล์เริ่มต้นคือ `main`)
2. **Import**: การนำเข้า library อื่นมาใช้งาน
3. **Function main()**: จุดเริ่มต้นการทำงานของโปรแกรม

### ตัวอย่างโค้ด: Hello World
```go
package main

import "fmt"

func main() {
    fmt.Println("สวัสดี Go!")
}
```

## การรันโปรแกรม (Running Go Code)
เราสามารถใช้คำสั่งผ่าน terminal เพื่อรันหรือ build โปรแกรมได้:

- **Run โดยตรง**: `go run hello.go`
- **Build เป็นไฟล์ executable**: `go build hello.go`

## ตัวแปรและการประกาศ (Variables)
Go เป็นภาษาแบบ Static Type แต่มีความยืดหยุ่นในการประกาศตัวแปร

```go
package main

import "fmt"

func main() {
    // ประกาศแบบระบุ Type
    var message string = "Hello Go"
    
    // ประกาศแบบสั้น (Short Declaration) - Go จะเดา Type ให้เอง
    count := 10
    
    fmt.Println(message)
    fmt.Printf("จำนวนคือ: %d\n", count)
}
```

## จุดเด่นที่ควรรู้
- **Compiled Language**: แปลงเป็น Machine Code โดยตรง ทำให้ทำงานเร็ว
- **Garbage Collection**: จัดการหน่วยความจำให้อัตโนมัติ
- **Strongly Typed**: ตรวจสอบชนิดข้อมูลเข้มงวด ช่วยลด Bug

## อ้างอิง
- [[Summary - Mastering Go 4th Edition]], Chapter 1.
