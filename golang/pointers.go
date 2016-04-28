package main

import "fmt"

func pointer(cnt int, somevar* int) {
  for i := 0; i < cnt; i++ {
    *somevar++
  }
  return
}

func main() {
  blah := 0
  pointer(50, &blah)
  fmt.Println(blah)
}
