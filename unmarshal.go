/*
 * Copyright 2016 Chris Cartland. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

type UnstructuredJSON struct {
	Map map[string]interface{} `json:???` // Rest of the fields should go here.
}

type _UnstructuredJSON UnstructuredJSON

func (f *UnstructuredJSON) UnmarshalJSON(bs []byte) (err error) {
	foo := _UnstructuredJSON{}

	if err = json.Unmarshal(bs, &foo); err == nil {
		*f = UnstructuredJSON(foo)
	}

	m := make(map[string]interface{})

	if err = json.Unmarshal(bs, &m); err == nil {
		f.Map = m
	}

	return err
}

func ParseFile(filename string) UnstructuredJSON {
	file, e := ioutil.ReadFile(filename)
	if e != nil {
		fmt.Printf("File error: %v\n", e)
		os.Exit(1)
	}
	var jsonvar UnstructuredJSON
	json.Unmarshal(file, &jsonvar)
	return jsonvar
}

func parseFile(filename string) UnstructuredJSON {
	file, e := ioutil.ReadFile(filename)
	if e != nil {
		fmt.Printf("File error: %v\n", e)
		os.Exit(1)
	}
	var jsonvar UnstructuredJSON
	json.Unmarshal(file, &jsonvar)
	return jsonvar
}

func main() {
	s := parseFile("./short.json")
	fmt.Printf("Results: %v\n", s)
}
