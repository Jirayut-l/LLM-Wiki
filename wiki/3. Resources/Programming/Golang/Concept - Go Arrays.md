---
tags:
  - golang
  - concept
  - programming
---

# Concept - Go Arrays (แถวลำดับในภาษา Go)

## สารบัญ (Table of Contents)
- [1. Syntax (ไวยากรณ์)](#1-syntax-ไวยากรณ์)
- [2. Example when to use (ตัวอย่างกรณีที่ควรใช้งาน)](#2-example-when-to-use-ตัวอย่างกรณีที่ควรใช้งาน)
- [3. Initialization (การกำหนดค่าเริ่มต้น)](#3-initialization-การกำหนดค่าเริ่มต้น)
- [4. Accessing Elements (การเข้าถึงสมาชิก)](#4-accessing-elements-การเข้าถึงสมาชิก)
- [5. Iterating Over Arrays (การวนลูปอ่านข้อมูล)](#5-iterating-over-arrays-การวนลูปอ่านข้อมูล)
- [6. Multidimensional Arrays (แถวลำดับหลายมิติ)](#6-multidimensional-arrays-แถวลำดับหลายมิติ)
- [7. Length (การตรวจสอบขนาด)](#7-length-การตรวจสอบขนาด)
- [8. Passing Arrays to Functions (การส่ง Array เข้าฟังก์ชัน)](#8-passing-arrays-to-functions-การส่ง-array-เข้าฟังก์ชัน)
- [9. Zero Values in Arrays (ค่าเริ่มต้นของ Array)](#9-zero-values-in-arrays-ค่าเริ่มต้นของ-array)
- [10. Comparing Arrays (การเปรียบเทียบ Array)](#10-comparing-arrays-การเปรียบเทียบ-array)
- [แหล่งอ้างอิงและลิงก์ที่เกี่ยวข้อง](#แหล่งอ้างอิงและลิงก์ที่เกี่ยวข้อง)

Array คือชุดของข้อมูลประเภทเดียวกันที่มี **ขนาดคงที่ (Fixed Length)** ซึ่งขนาดของ Array ถือเป็นส่วนหนึ่งของชนิดข้อมูล (Type) ด้วย

## 1. Syntax (ไวยากรณ์)
การประกาศ Array ใน Go ใช้รูปแบบดังนี้:
```go
var variableName [length]Type
```
โดยที่ `length` คือจำนวนสมาชิก และ `Type` คือชนิดของข้อมูล

## 2. Example when to use (ตัวอย่างกรณีที่ควรใช้งาน)
เราควรใช้ Array เมื่อทราบจำนวนข้อมูลที่แน่นอนและ **ไม่มีการเปลี่ยนแปลงขนาด** ตลอดการทำงานของโปรแกรม เพื่อความเร็วสูงสุดในการประมวลผลและประหยัดหน่วยความจำ

### ตัวอย่างการใช้งานจริง:
```go
package main

import "fmt"

func main() {
    // 1. วันในหนึ่งสัปดาห์ (ข้อมูลคงที่ 7 วัน)
    days := [7]string{
        "Monday", "Tuesday", "Wednesday", 
        "Thursday", "Friday", "Saturday", "Sunday",
    }
    
    // 2. ทิศทางหลัก (ข้อมูลคงที่ 4 ทิศ)
    directions := [4]string{"North", "South", "East", "West"}
    
    // 3. ค่าสี RGB (ข้อมูลคงที่ 3 ค่า: R, G, B)
    redColor := [3]int{255, 0, 0}
    
    fmt.Println("Days:", days)
    fmt.Println("Directions:", directions)
    fmt.Printf("RGB Red: %v\n", redColor)
}
```

## 3. Initialization (การกำหนดค่าเริ่มต้น)
เราสามารถกำหนดค่าให้ Array ได้หลายวิธี:

### แบบใช้คีย์เวิร์ด `var` (จะได้ Zero Values)
```go
var numbers [5]int // จะได้ [0 0 0 0 0]
```

### แบบ Array Literal (กำหนดค่าทันที)
```go
numbers := [3]int{10, 20, 30}
```

### แบบให้ Go นับจำนวนสมาชิกให้อัตโนมัติด้วย `...`
```go
colors := [...]string{"Red", "Green", "Blue"} // Go จะกำหนดขนาดเป็น [3] อัตโนมัติ
```

### แบบกำหนดค่าเฉพาะบางตำแหน่ง (Sparse Array)
```go
// กำหนด index ที่ 0 เป็น 1 และ index ที่ 3 เป็น 10 ส่วนที่เหลือเป็น 0
nums := [5]int{0: 1, 3: 10} 
```

## 4. Accessing Elements (การเข้าถึงสมาชิก)
เราสามารถเข้าถึงและแก้ไขสมาชิกใน Array ผ่านทาง Index (เริ่มที่ 0)

### การอ่านค่า (Reading)
```go
val := numbers[0]
```
### การเข้าถึงและแก้ไขค่า (Accessing & Modifying)
```go
numbers[0] = 10              // กำหนดค่า
fmt.Println(numbers[0])      // อ่านค่า
```

## 5. Iterating Over Arrays (การวนลูปอ่านข้อมูลแบบละเอียด)
การวนลูป (Looping) คือหัวใจสำคัญของการจัดการข้อมูลใน Array ซึ่งในภาษา Go มี 2 วิธีหลักที่นักศึกษาควรทราบ:

### วิธีที่ 1: การใช้ Standard `for` Loop
วิธีนี้เหมาะสำหรับกรณีที่เราต้องการควบคุม Index อย่างละเอียด เช่น การวนลูปถอยหลัง หรือการข้ามทีละหลายตำแหน่ง

**Syntax:**
```go
for i := 0; i < len(arr); i++ {
    // arr[i] คือการเข้าถึงสมาชิกตัวที่ i
}
```

### วิธีที่ 2: การใช้ `for range` (แนะนำสำหรับเด็กปี 1)
วิธีนี้คือ **"Go Idiomatic"** (วิธีที่คนเขียน Go นิยมที่สุด) เพราะอ่านง่ายและป้องกันปัญหา "Index Out of Bounds" (ลูปเกินขนาด)

**Syntax มี 3 รูปแบบหลัก:**

1. **เอาทั้ง Index และ Value:**
```go
for index, value := range arr {
    fmt.Printf("ตำแหน่งที่ %d มีค่าคือ %v\n", index, value)
}
```

2. **เอาเฉพาะ Index (ไม่เอา Value):**
```go
for index := range arr {
    fmt.Println("Index:", index)
}
```

3. **เอาเฉพาะ Value (ใช้ Blank Identifier `_` ปิด Index ไว้):**
```go
for _, value := range arr {
    fmt.Println("Value:", value)
}
```

**TL;DR:** ถ้าต้องการแค่อ่านข้อมูลทุกตัว ให้ใช้ `for range` เสมอ เพราะมันทั้งคลีนและปลอดภัยกว่าครับ!


## 6. Multidimensional Arrays (แถวลำดับหลายมิติ)
เราสามารถสร้าง Array ซ้อน Array ได้ (เช่น ตาราง 2 มิติ หรือ Grid):

```go
// การประกาศ Array 2 มิติ [แถว][คอลัมน์]
var matrix [2][3]int 

matrix = [2][3]int{
    {1, 2, 3},
    {4, 5, 6},
}
```

## 7. Length (การตรวจสอบขนาด)
เราใช้ฟังก์ชัน `len()` เพื่อหาขนาดของ Array:
```go
colors := [3]string{"Red", "Blue", "Green"}
fmt.Println(len(colors)) // ผลลัพธ์: 3
```
**จำไว้ว่า:** ขนาดของ Array ใน Go เปลี่ยนแปลงไม่ได้หลังจากประกาศไปแล้ว

## 8. Passing Arrays to Functions (การส่ง Array เข้าฟังก์ชัน)
ใน Go เมื่อเราส่ง Array เข้าไปในฟังก์ชัน มันจะเป็นการ **"คัดลอก (Copy)"** ข้อมูลทั้งหมดเข้าไปใหม่:
- **ข้อเสีย:** หาก Array มีขนาดใหญ่มาก จะกินหน่วยความจำและทำงานช้าลง
- **วิธีแก้:** ในการทำงานจริง นิยมใช้ [[Concept - Go Composite Data Types#Slice|Slice]] แทนเพราะส่งค่าเป็น Reference (ประหยัดกว่า)

```go
func updateArray(arr [3]int) {
    arr[0] = 99 // เปลี่ยนแปลงเฉพาะใน Copy ไม่กระทบตัวจริงข้างนอก
}
```

## 9. Zero Values in Arrays (ค่าเริ่มต้นของ Array)
เมื่อประกาศ Array โดยไม่ระบุค่า Go จะกำหนด **Zero Value** ให้สมาชิกทุกตัวตามชนิดข้อมูล:
- `int` -> `0`
- `string` -> `""`
- `bool` -> `false`

## 10. Comparing Arrays (การเปรียบเทียบ Array)
เราสามารถใช้ `==` และ `!=` เปรียบเทียบ Array สองตัวได้ **ก็ต่อเมื่อ**:
1. ทั้งคู่มี **Type เดียวกัน** (ชนิดข้อมูลเหมือนกัน)
2. ทั้งคู่มี **ขนาดเท่ากัน** (เช่น `[3]int` เปรียบเทียบกับ `[3]int` ได้ แต่เปรียบเทียบกับ `[5]int` ไม่ได้)

---
## แหล่งอ้างอิงและลิงก์ที่เกี่ยวข้อง
- [[Concept - Go Data Types]]: ข้อมูลพื้นฐานใน Go
- [[Concept - Go Composite Data Types]]: ประเภทข้อมูลแบบผสมอื่นๆ (Slice, Map, Struct)
