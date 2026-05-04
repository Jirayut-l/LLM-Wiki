---
tags:
  - golang
  - concept
  - programming
---

# Concept - Go Data Types

ข้อมูลพื้นฐานเกี่ยวกับประเภทข้อมูล (Data Types) ในภาษา Go ซึ่งเป็นภาษาแบบ Static Typing ที่ต้องการการระบุประเภทข้อมูลอย่างชัดเจน.

## ประเภทข้อมูลพื้นฐาน (Basic Data Types)

ภาษา Go แบ่งประเภทข้อมูลหลักๆ ได้ดังนี้:

### 1. เลขจำนวนเต็ม (Integers)
- `int`: ขนาดขึ้นอยู่กับสถาปัตยกรรมเครื่อง (32 หรือ 64 บิต)
- `int8`, `int16`, `int32`, `int64`: ระบุขนาดบิตแน่นอนแบบมีเครื่องหมาย
- `uint`, `uint8`, `uint16`, `uint32`, `uint64`: ระบุขนาดบิตแน่นอนแบบไม่มีเครื่องหมาย (บวกเท่านั้น)
- `byte`: ชื่อเรียกเล่น (Alias) ของ `uint8`
- `rune`: ชื่อเรียกเล่นของ `int32` (ใช้เก็บค่า Unicode)

### 2. เลขทศนิยม (Floating Point Numbers)
- `float32`: ทศนิยมขนาด 32 บิต
- `float64`: ทศนิยมขนาด 64 บิต (แนะนำให้ใช้เป็นค่าเริ่มต้น)

### 3. ค่าความจริง (Boolean)
- `bool`: เก็บค่า `true` หรือ `false`

### 4. ข้อความ (String)
- `string`: ชุดของตัวอักษร (Sequence of bytes) โดยปกติจะเป็น UTF-8

### 5. จำนวนเชิงซ้อน (Complex Numbers)
- `complex64`, `complex128`

## ตัวอย่างรหัสต้นฉบับ (Example Code)

```go
package main

import "fmt"

func main() {
    // 1. Integer
    var age int = 25
    var population uint = 1000000

    // 2. Floating Point
    var price float64 = 99.50
    pi := 3.14159 // Short declaration (Go assumes float64)

    // 3. Boolean
    var isReady bool = true

    // 4. String
    var name string = "Gopher"
    message := "Hello, Go!"

    fmt.Printf("Age: %d, Type: %T\n", age, age)
    fmt.Printf("Price: %.2f, Type: %T\n", price, price)
    fmt.Printf("Is Ready: %t, Type: %T\n", isReady, isReady)
    fmt.Printf("Name: %s, Type: %T\n", name, name)
}
```

## แหล่งอ้างอิงและลิงก์ที่เกี่ยวข้อง
- [[Concept - Go Introduction]]
- [[Summary - Mastering Go 4th Edition]]
