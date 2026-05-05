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
- [5. Iterating Over Arrays (การวนลูปอ่านข้อมูลแบบละเอียด)](#5-iterating-over-arrays-การวนลูปอ่านข้อมูลแบบละเอียด)
- [6. Multidimensional Arrays (แถวลำดับหลายมิติ)](#6-multidimensional-arrays-แถวลำดับหลายมิติ)
- [7. Length (การตรวจสอบขนาด)](#7-length-การตรวจสอบขนาด)
- [8. Passing Arrays to Functions (การส่ง Array เข้าฟังก์ชัน)](#8-passing-arrays-to-functions-การส่ง-array-เข้าฟังก์ชัน)
    - [8.1 การส่งแบบ Array (Copy)](#81-การส่งแบบ-array-copy)
    - [8.2 Best Practice: ใช้ Slice แทน (Reference-like)](#82-best-practice-ใช้-slice-แทน-reference-like)
- [9. Zero Values in Arrays (ค่าเริ่มต้นของ Array)](#9-zero-values-in-arrays-ค่าเริ่มต้นของ-array)
    - [9.1 ตารางค่าเริ่มต้น (Default Values)](#91-ตารางค่าเริ่มต้น-default-values)
    - [9.2 ตัวอย่างการใช้งานและ Best Practice](#92-ตัวอย่างการใช้งานและ-best-practice)
- [10. Comparing Arrays (การเปรียบเทียบ Array)](#10-comparing-arrays-การเปรียบเทียบ-array)
    - [10.1 เงื่อนไขการเปรียบเทียบ](#101-เงื่อนไขการเปรียบเทียบ)
    - [10.2 Scenario ในโปรเจกต์ใหญ่ (Real-world Use Case)](#102-scenario-ในโปรเจกต์ใหญ่-real-world-use-case)
    - [10.3 ข้อควรระวัง (Slice vs Array)](#103-ข้อควรระวัง-slice-vs-array)
    - [10.4 การใช้ reflect.DeepEqual (ทางเลือกสำหรับกรณีพิเศษ)](#104-การใช้-reflectdeepequal-ทางเลือกสำหรับกรณีพิเศษ)
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
นี่คือเรื่องที่นักศึกษาต้องระวังให้มากครับ! ในภาษา Go เวลาเราส่ง Array เข้าไปในฟังก์ชัน มันจะทำงานแบบ **"Pass by Value"** เสมอ

### 8.1 การส่งแบบ Array (Copy)
เมื่อส่ง Array เข้าไป Go จะ **"ก๊อปปี้"** ข้อมูลทั้งหมดใน Array นั้นขึ้นมาใหม่ในฟังก์ชัน
- **ผลลัพธ์:** การแก้ไขค่าในฟังก์ชันจะ **ไม่กระทบ** ตัวแปรต้นฉบับข้างนอก
- **ความเสี่ยง:** หาก Array มีขนาดใหญ่ (เช่น 1 ล้านสมาชิก) การก๊อปปี้จะทำให้โปรแกรมทำงานช้ามาก

```go
func modifyArray(arr [3]int) {
    arr[0] = 999
    fmt.Println("ในฟังก์ชัน:", arr) // [999 2 3]
}

func main() {
    myArr := [3]int{1, 2, 3}
    modifyArray(myArr)
    fmt.Println("นอกฟังก์ชัน:", myArr) // [1 2 3] (ค่าไม่เปลี่ยน!)
}
```

### 8.2 Best Practice: ใช้ Slice แทน (Reference-like)
ในการทำงานจริง เราแทบไม่ส่ง Array เข้าฟังก์ชันเลย แต่เราจะใช้ **Slice** แทนครับ เพราะ Slice ส่งแค่ "Pointer" (ตัวชี้) ไปหาข้อมูลจริง ไม่ได้ก๊อปปี้ข้อมูลทั้งหมด

```go
// รับค่าเป็น Slice (ไม่ระบุขนาดใน [])
func modifySlice(s []int) {
    s[0] = 999 
}

func main() {
    myArr := [3]int{1, 2, 3}
    // ส่ง myArr[:] เพื่อแปลง Array เป็น Slice (เรียกว่า Slice Operator)
    modifySlice(myArr[:]) 
    fmt.Println("หลังใช้ Slice:", myArr) // [999 2 3] (ค่าเปลี่ยนทันที!)
}
```

**Rule of Thumb:**
- **ใช้ Array** เมื่อต้องการความมั่นใจว่าข้อมูลต้นฉบับจะ "ไม่ถูกแก้ไข" แน่นอน (Immutability)
- **ใช้ Slice** เป็นค่าเริ่มต้น (Default) สำหรับงานเกือบทั้งหมด เพราะประสิทธิภาพสูงกว่าและยืดหยุ่นกว่าครับ

## 9. Zero Values in Arrays (ค่าเริ่มต้นของ Array)
ในภาษา Go เราไม่ต้องกลัวเรื่อง "Garbage Data" (ข้อมูลขยะที่ค้างในหน่วยความจำ) ครับ เพราะ Go จะล้างข้อมูลและเติม **Zero Value** ให้เราทันทีที่ประกาศ Array

### 9.1 ตารางค่าเริ่มต้น (Default Values)
| ชนิดข้อมูล | Zero Value |
| :--- | :--- |
| `int`, `float` | `0` หรือ `0.0` |
| `string` | `""` (String ว่าง) |
| `bool` | `false` |
| `pointer`, `slice`, `map` | `nil` |

### 9.2 ตัวอย่างการใช้งานและ Best Practice
```go
var scores [5]int 
// Go เติม [0 0 0 0 0] ให้ทันที ไม่ต้องเขียน scores = [5]int{0,0,0,0,0} เอง!

// การตรวจสอบว่าข้อมูลถูกเติมหรือยัง (Checking status)
if scores[0] == 0 {
    fmt.Println("ตำแหน่งนี้ยังไม่มีข้อมูลใหม่ถูกเขียนทับ (ยังเป็นค่าเริ่มต้น)")
}
```

**Best Practice:**
- **อย่าเขียนโค้ดซ้ำซ้อน:** ถ้าคุณต้องการ Array ที่เริ่มต้นด้วย 0 อยู่แล้ว ให้ใช้ `var arr [N]Type` แทนการใช้ Literal `arr := [N]Type{0, 0, ...}` เพื่อความคลีนของโค้ด
- **ใช้ Zero Value ให้เป็นประโยชน์:** เช่น ในระบบโหวต ถ้าคะแนนเริ่มต้นเป็น 0 เราสามารถเริ่มนับได้ทันทีโดยไม่ต้องเสียเวลาลูปเพื่อ Reset ค่าครับ

## 10. Comparing Arrays (การเปรียบเทียบ Array)
ใน Go เราสามารถใช้ `==` และ `!=` เพื่อดูว่าสมาชิกทุกตัวในสอง Array "เหมือนกันเป๊ะ" หรือไม่ครับ แต่มันมีเงื่อนไขสำคัญที่นักศึกษาต้องจำให้ขึ้นใจ:

### 10.1 เงื่อนไขการเปรียบเทียบ
1. **ต้องเป็น Type เดียวกัน:** เช่น `int` เหมือนกัน
2. **ต้องมีขนาด (Length) เท่ากัน:** เพราะใน Go ขนาดคือส่วนหนึ่งของ Type (เช่น `[3]int` กับ `[5]int` คือคนละชนิดข้อมูลกันเลย!)

```go
a := [3]int{1, 2, 3}
b := [3]int{1, 2, 3}
c := [3]int{1, 2, 4}

fmt.Println(a == b) // true (เหมือนกันทุกตัว)
fmt.Println(a == c) // false (ตัวสุดท้ายไม่เหมือน)

// d := [2]int{1, 2}
// fmt.Println(a == d) // Compile Error! เพราะ [3]int เทียบกับ [2]int ไม่ได้
```

### 10.2 Scenario ในโปรเจกต์ใหญ่ (Real-world Use Case)
ในระบบขนาดใหญ่ เรามักใช้การเปรียบเทียบ Array ในกรณีที่ต้องการความเร็วสูงและโครงสร้างที่แน่นอน:

**ตัวอย่างที่ 1: การเช็ค Checksum (Security)**
```go
// สมมติค่า Hash ของไฟล์ที่ถูกต้อง
expectedHash := [32]byte{0xaf, 0x12, ..., 0x99} 
actualHash := getFileHash("data.txt")

if actualHash == expectedHash {
    fmt.Println("ไฟล์ถูกต้อง ไม่ถูกแก้ไข")
}
```

**ตัวอย่างที่ 2: การเปรียบเทียบ Game State (Game Dev)**
```go
// [HP, MP, Level, EXP]
oldStats := [4]int{100, 50, 1, 0}
newStats := [4]int{100, 50, 1, 0}

if oldStats == newStats {
    fmt.Println("ไม่มีการเปลี่ยนแปลงของตัวละครใน Frame นี้ (ไม่ต้อง Update UI)")
}
```

### 10.3 ข้อควรระวัง (Slice vs Array)
นี่คือจุดที่คนสับสนบ่อยที่สุดครับ:
- **Array:** เปรียบเทียบด้วย `==` ได้ทันที
- **Slice:** เปรียบเทียบด้วย `==` **ไม่ได้** (ยกเว้นเทียบกับ `nil`)

**ตัวอย่างความแตกต่าง:**
```go
// 1. Array (เปรียบเทียบได้เลย)
arr1 := [2]int{1, 2}
arr2 := [2]int{1, 2}
fmt.Println(arr1 == arr2) // Output: true

// 2. Slice (เปรียบเทียบด้วย == ไม่ได้!)
slc1 := []int{1, 2}
slc2 := []int{1, 2}
// fmt.Println(slc1 == slc2) // Compile Error: invalid operation (slice can only be compared to nil)

// วิธีแก้: ต้องใช้ reflect.DeepEqual หรือวนลูปเทียบเอง
fmt.Println(reflect.DeepEqual(slc1, slc2)) // Output: true
```

**Rule of Thumb:** ถ้าคุณมีข้อมูลที่ "ขนาดไม่เปลี่ยน" และต้อง "เปรียบเทียบกันบ่อยๆ" การใช้ Array จะช่วยให้โค้ดของคุณสั้นและทำงานเร็วมากครับ!

### 10.4 การใช้ reflect.DeepEqual (ทางเลือกสำหรับกรณีพิเศษ)
ในบางกรณีที่ซับซ้อนมาก หรือเราต้องการเปรียบเทียบข้อมูลที่ "เราไม่รู้ชนิดข้อมูลที่แน่นอน" ในตอนเขียนโปรแกรม เราสามารถใช้ฟังก์ชัน `DeepEqual` จากแพ็กเกจ `reflect` ได้ครับ

```go
import (
    "fmt"
    "reflect"
)

func main() {
    a := [3]int{1, 2, 3}
    b := [3]int{1, 2, 3}

    // ใช้ DeepEqual เปรียบเทียบ
    isEqual := reflect.DeepEqual(a, b)
    fmt.Println("DeepEqual:", isEqual) // true
}
```

**คำแนะนำ:**
- **ข้อดี:** มันทรงพลังมาก เปรียบเทียบได้ทุกอย่าง (Array, Slice, Map, Struct)
- **ข้อเสีย (สำคัญมาก):** มันทำงาน **ช้ากว่า** การใช้ `==` หลายเท่าตัว เพราะต้องใช้เทคนิค "Reflection" เพื่อแกะดูข้อมูลข้างในทีละตัว
- **สรุป:** ถ้าเป็น Array ปกติ ให้ใช้ `==` เสมอครับ แต่ถ้าต้องทำโปรแกรมที่ยืดหยุ่นมากๆ (Generic-like) ค่อยนึกถึง `reflect.DeepEqual` นะครับนักศึกษา

---
## แหล่งอ้างอิงและลิงก์ที่เกี่ยวข้อง
- [[Concept - Go Data Types]]: ข้อมูลพื้นฐานใน Go
- [[Concept - Go Composite Data Types]]: ประเภทข้อมูลแบบผสมอื่นๆ (Slice, Map, Struct)
