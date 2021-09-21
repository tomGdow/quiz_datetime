import problems_quiz as p

codes = {
        "a": "%a",
        "A": "%A",
        "b": "%b",
        "B": "%B",
        "c": "%c",
        "d": "%d",
        "f": "%f",
        "H": "%H",
        "I": "%I",
        "j": "%j",
        "m": "%m",
        "M": "%M",
        "p": "%p",
        "S": "%S",
        "U": "%U",
        "w": "%w",
        "W": "%W",
        "x": "%x",
        "X": "%X",
        "y": "%y",
        "Y": "%Y",
        "z": "%z",
        "Z": "%Z",
        # "e" :"e" 
        }

explanation = {
        "a": ["%a", "Weekday as locale’s abbreviated name", "Sun"],
        "A": ["%A", "Weekday as locale’s full name", "Sunday"],
        "b": ["%b", "Month as locale’s abbreviated name", "Sep"],
        "B": ["%B", "Month as locale’s full name", "September"],
        "c": ["%c", "Locale’s appropriate date and time representation","Sun Sep 8 07:06:05 2013"],
        "d": ["%d", "Day of the month as a zero-padded decimal number.","8"],
        "f": ["%f", "Microsecond as a decimal number, zero-padded on the left", "000000"],
        "H": ["%H", "Hour (24-hour clock) as a zero-padded decimal number","08"],
        "I": ["%I", "Hour (12-hour clock) as a zero-padded decimal number","05"],
        "j": ["%j", "Day of the year as a zero-padded decimal number","282"],
        "m": ["%m", "Month as a zero-padded decimal number.","09"],
        "M": ["%M", "Minute as a zero-padded decimal number", "04"],
        "p": ["%p", "Locale’s equivalent of either AM or PM", "PM"],
        "S": ["%S", "Second as a zero-padded decimal number", "03"],
        "U": ["%U", "Week number of the year (Sunday as the first day of the week) as a zero padded decimal number", "32"],          "w": ["%w", "Weekday as a decimal number, where 0 is Sunday and 6 is Saturday","0"],
        "W": ["%W", "Week number of the year (Monday as the first day of the week) as a decimal number", "35"],
        "x": ["%x", "Locale’s appropriate date representation", "09/08/13"],
        "X": ["%X", "Locale’s appropriate time representation","07:06:05"],                                                                                            
        "y": ["%y", "Year without century as a zero-padded decimal number","13"],
        "Y": ["%Y", "Year with century as a decimal number","2013"],
        "z": ["%z", "UTC offset in the form ±HHMM[SS[.ffffff]]","+0000"],
        "Z": ["%Z","Time zone name (empty string if the object is naive)","UTC"],
        "" : ["",""] 
        }


example = {
        "a": ["%a", "datetime.datetime.strftime(datetime.datetime.now(), '%a')", "Tue"],
        "A": ["%A", "datetime.datetime.strftime(datetime.datetime.now(), '%A')", "Tuesday"],
        "b": ["%b", "datetime.datetime.strftime(datetime.datetime.now(), '%b')", 'Sep'],
        "B": ["%B", "datetime.datetime.strftime(datetime.datetime.now(), '%B')", 'September'],
        "c": ["%c", "datetime.datetime.strftime(datetime.datetime.now(), '%c')", "Tue Sep 21 01:01:47 2021"],
        "d": ["%d", "datetime.datetime.strftime(datetime.datetime.now(), '%d')", "21"],
        "f": ["%f", "datetime.datetime.strftime(datetime.datetime.now(), '%f')", "124670"],
        "H": ["%H", "datetime.datetime.strftime(datetime.datetime.now(), '%H')", "01"],
        "I": ["%I", "datetime.datetime.strftime(datetime.datetime.now(), '%I')", "01"],
        "j": ["%j", "datetime.datetime.strftime(datetime.datetime.now(), '%j')", "263"], 
        "m": ["%m", "datetime.datetime.strftime(datetime.datetime.now(), '%m')", "09"],
        "M": ["%M", "datetime.datetime.strftime(datetime.datetime.now(), '%M')", "15"],
        "p": ["%p", "datetime.datetime.strftime(datetime.datetime.now(), '%p')", "AM"],
        "S": ["%S", "datetime.datetime.strftime(datetime.datetime.now(), '%S')", "22"],
        "U": ["%U", "datetime.datetime.strftime(datetime.datetime.now(), '%U')", "38"],
        "w": ["%w", "datetime.datetime.strftime(datetime.datetime.now(), '%w')", "2"],
        "W": ["%W", "datetime.datetime.strftime(datetime.datetime.now(), '%W')", "38"],
        "x": ["%x", "datetime.datetime.strftime(datetime.datetime.now(), '%x')", "09/21/21"],
        "X": ["%X", "datetime.datetime.strftime(datetime.datetime.now(), '%X')", "01:24:28"],
        "y": ["%y", "datetime.datetime.strftime(datetime.datetime.now(), '%y')", "21"],
        "Y": ["%Y", "datetime.datetime.strftime(datetime.datetime.now(), '%Y')", "2021"],
        "z": ["%z", "datetime.datetime.strftime(datetime.datetime.now(datetime.timezone.utc), '%z')", "+0000"],
        "Z": ["%Z", "datetime.datetime.strftime(datetime.datetime.now(datetime.timezone.utc), '%Z')", "UTC"],
        # "e" :"%e"    
        }


