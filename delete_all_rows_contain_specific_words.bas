Attribute VB_Name = "delete_specific_rows"
Sub delete_all_rows_contain_specific_words()
c = [{"中兴", "自拍"}]
Application.ScreenUpdating = False
For Each sh In Sheets
    With sh
        arr = .UsedRange.Value
        For i = UBound(arr) To 1 Step -1
            flag = False
            For j = 1 To UBound(arr, 2)
                For k = 1 To UBound(c)
                    If InStr(arr(i, j), c(k)) > 0 Then
                        flag = True: .Rows(i).Delete: Exit For
                    End If
                Next
                If flag Then Exit For
            Next
        Next
    End With
Next
MsgBox "Finish!"
End Sub
