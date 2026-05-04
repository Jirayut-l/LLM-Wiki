---
tags:
  - golang
  - concept
  - programming
---

# Concept - Go Data Types (ประเภทข้อมูลในภาษา Go)

## สารบัญ (Table of Contents)
- [ประเภทข้อมูลพื้นฐาน (Basic Data Types)](#ประเภทข้อมูลพื้นฐาน-basic-data-types)
  - [1. เลขจำนวนเต็ม (Integers)](#1-เลขจำนวนเต็ม-integers)
  - [2. เลขทศนิยม (Floating Point Numbers)](#2-เลขทศนิยม-floating-point-numbers)
  - [3. ค่าความจริง (Boolean)](#3-ค่าความจริง-boolean)
  - [4. ข้อความ (String)](#4-ข้อความ-string)
- [ตัวอย่างรหัสต้นฉบับแบบละเอียด (Detailed Examples)](#ตัวอย่างรหัสต้นฉบับแบบละเอียด-detailed-examples)
  - [การใช้งาน Integer และ Overflow เบื้องต้น](#การใช้งาน-integer-และ-overflow-เบื้องต้น)
  - [การใช้งาน Floating Point และความแม่นยำ](#การใช้งาน-floating-point-และความแม่นยำ)
  - [การใช้งาน String และ Multi-line](#การใช้งาน-string-และ-multi-line)
  - [ค่าเริ่มต้น (Zero Values)](#ค่าเริ่มต้น-zero-values)
- [สรุปคำแนะนำสำหรับผู้เริ่มต้น](#สรุปคำแนะนำสำหรับผู้เริ่มต้น)
- [แหล่งอ้างอิงและลิงก์ที่เกี่ยวข้อง](#แหล่งอ้างอิงและลิงก์ที่เกี่ยวข้อง)

ทำความเข้าใจประเภทข้อมูลพื้นฐานในภาษา Go ซึ่งเป็นภาษาประเภท **Static Typing** (ต้องรู้ชนิดข้อมูลตั้งแต่ตอนเขียนโปรแกรม) และ **Strongly Typed** (ไม่สามารถเปลี่ยนชนิดข้อมูลไปมาได้โดยไม่แปลงค่าก่อน).

## ประเภทข้อมูลพื้นฐาน (Basic Data Types)

### 1. เลขจำนวนเต็ม (Integers)
แบ่งออกเป็นแบบมีเครื่องหมาย (Signed) และไม่มีเครื่องหมาย (Unsigned):

- **แบบระบุขนาดแน่นอน**: 
    - `int8`, `int16`, `int32`, `int64` (เก็บค่าลบถึงบวก)
    - `uint8`, `uint16`, `uint32`, `uint64` (เก็บค่าบวกเท่านั้น)
- **แบบตามสถาปัตยกรรม (Platform Dependent)**:
    - `int` และ `uint`: จะมีขนาด 32 บิตในระบบ 32-bit และ 64 บิตในระบบ 64-bit (แนะนำให้ใช้ `int` เป็นหลักสำหรับจำนวนทั่วไป)
- **ตัวย่อพิเศษ (Aliases)**:
    - `byte`: มีค่าเท่ากับ `uint8` (นิยมใช้กับข้อมูลดิบหรือไฟล์)
    - `rune`: มีค่าเท่ากับ `int32` (ใช้เก็บตัวอักษร Unicode หนึ่งตัว)

### 2. เลขทศนิยม (Floating Point Numbers)
- `float32`: ความแม่นยำระดับหลักทศนิยมประมาณ 7 ตำแหน่ง
- `float64`: ความแม่นยำระดับหลักทศนิยมประมาณ 15 ตำแหน่ง (**นิยมใช้ที่สุด**)

### 3. ค่าความจริง (Boolean)
- `bool`: มีเพียงสองค่าคือ `true` (จริง) หรือ `false` (เท็จ) มักใช้ในการตรวจสอบเงื่อนไข `if-else`.

### 4. ข้อความ (String)
- `string`: คือชุดของตัวอักษรที่แก้ไขไม่ได้ (Immutable) ถูกเก็บในรูปแบบ UTF-8 โดยปกติ.

---

## ตัวอย่างรหัสต้นฉบับแบบละเอียด (Detailed Examples)

### การใช้งาน Integer และ Overflow เบื้องต้น
```go
package main

import "fmt"

func main() {
    var a int = 100
    var b int8 = 127 // ค่าสูงสุดของ int8
    
    fmt.Printf("Value a: %v, Type: %T\n", a, a)
    fmt.Printf("Max int8: %v\n", b)
    
    // การแปลงชนิดข้อมูล (Type Conversion)
    // Go จะไม่ยอมให้บวกคนละ Type กันตรงๆ เช่น int + int8
    sum := a + int(b) 
    fmt.Println("Sum:", sum)
}
```

### การใช้งาน Floating Point และความแม่นยำ
```go
package main

import "fmt"

func main() {
    price := 99.99     // Go จะเดาว่าเป็น float64 อัตโนมัติ
    var tax float32 = 0.07
    
    // ต้องแปลง float32 เป็น float64 ก่อนคำนวณร่วมกัน
    total := price + float64(tax)
    
    fmt.Printf("Total: %.2f\n", total)
}
```

### การใช้งาน String และ Multi-line
```go
package main

import "fmt"

func main() {
    name := "Gopher"
    
    // String ปกติ (Interpret string)
    msg := "Hello, " + name + "!\nWelcome to Go."
    
    // Raw String Literal (เก็บตามที่พิมพ์ รวมถึงการขึ้นบรรทัดใหม่)
    longMsg := `
        This is a
        multi-line
        string in Go.
    `
    
    fmt.Println(msg)
    fmt.Println(longMsg)
    fmt.Println("ความยาวชื่อ:", len(name), "ตัวอักษร")
}
```

### ค่าเริ่มต้น (Zero Values)
ใน Go หากเราประกาศตัวแปรแล้วไม่กำหนดค่า มันจะมีค่าเริ่มต้นให้เสมอ:
- `int`, `float`: `0`
- `bool`: `false`
- `string`: `""` (ว่างเปล่า)

```go
var i int
var f float64
var b bool
var s string
fmt.Printf("Values: %v, %v, %v, %q\n", i, f, b, s) 
// ผลลัพธ์: Values: 0, 0, false, ""
```

---

## สรุปคำแนะนำสำหรับผู้เริ่มต้น
1. ใช้ `int` สำหรับเลขจำนวนเต็มทั่วไป เว้นแต่จะมีความจำเป็นต้องระบุขนาด
2. ใช้ `float64` สำหรับทศนิยมเสมอเพื่อความแม่นยำ
3. การคำนวณข้ามชนิดข้อมูล (เช่น `int` + `float64`) **ต้องทำ Type Conversion เสมอ**
4. ระวังเรื่อง **Case Sensitivity**: `myVar` กับ `MyVar` คือคนละตัวกัน (และมีผลเรื่องการเข้าถึงจากภายนอก package ด้วย)

## แหล่งอ้างอิงและลิงก์ที่เกี่ยวข้อง
- [[Concept - Go Introduction]]
- [[Summary - Mastering Go 4th Edition]]
