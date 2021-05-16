## Python-Script使用说明

1. 多个PDF文件统计页数

   括号内表示可选可不选，如果使用了该参数，那么程序在统计 PDF 时会递归地在所给目录的每个子目录中查找所有的 PDF 文件，否则的话只会统计在所给目录下的 PDF 文件。如果需要使用则把左右两边的括号删除即可。

   ```shell
   python3 count_pdf_pages.py /Users/tyfann/... (-r)
   ```

2. 多个pptx文件统计页数

   括号内表示可选可不选，如果使用了该参数，那么程序在统计 pptx 时会递归地在所给目录的每个子目录中查找所有的 pptx 文件，否则的话只会统计在所给目录下的 pptx 文件。如果需要使用则把左右两边的括号删除即可。

   ```shell
   python3 count_pptx_pages.py /Users/tyfann/... (-r)
   ```

   

