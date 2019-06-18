Sub Homework()
'loop through all sheets
Dim WS As Worksheet
    For Each WS In ActiveWorkbook.Worksheets
    WS.Activate
        ' make sure it reads all rows
        
          LastRow = WS.Cells(Rows.Count, 1).End(xlUp).Row

        'Declare the columns and variables for buckets
        
        Cells(1, "I").Value = "Ticker"
        Cells(1, "L").Value = "Total Stock Volume"
               
        Dim Ticker As String
        Dim TotalVolume As Double
        TotalVolume = 0
        Dim Row As Double
        Row = 2
        Dim Column As Integer
        Column = 1
        Dim Count As Long
        
         
        For Count = 2 To LastRow
         '
            If Cells(Count + 1, Column).Value <> Cells(Count, Column).Value Then
               
          
    
                Ticker = Cells(Count, Column).Value
                Cells(Row, Column + 8).Value = Ticker
                
                ' Add Total Volumn
                
                TotalVolume = TotalVolume + Cells(Count, Column + 6).Value
                Cells(Row, Column + 11).Value = TotalVolume
           
                Row = Row + 1
                '
                ' running total
                TotalVolume = 0
           
            Else
                TotalVolume = TotalVolume + Cells(Count, Column + 6).Value
            End If
        
        Next Count
    
    
        Next WS
        
End Sub
