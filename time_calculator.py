def add_time(start, duration, starting_day = False):
    weekDays = {1: 'Monday', 2:'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    new_time = ''
    
    splittedEntry = start.split()
    time = splittedEntry[0]
    format = splittedEntry[1]

    timeSplitted = time.split(':')
    hours = int(timeSplitted[0])
    minutes = int(timeSplitted[1])


    durationSplitted = duration.split(':')
    hourToSum = int(durationSplitted[0])
    minutesToSum = int(durationSplitted[1])

    totalMinutes = int(minutesToSum) + int(minutes)
    
    if totalMinutes == 60:
      hourToSum = hourToSum + 1
      totalMinutes = 0
    elif totalMinutes > 60:
      totalMinutes = totalMinutes - 60
      hourToSum = hourToSum + 1

    totalHours = hours + hourToSum

    totalHoursCopy = totalHours
    periodsOfTwelveHoursOverflow = 0
    isNextdays = False
  
    if totalHours > 12:
      totalHours = totalHours % 12
      periodsOfTwelveHoursOverflow = totalHoursCopy // 12
      
    isSameFormat = int(totalHoursCopy / 12) % 2 == 0

    if isSameFormat:
      finalFormat = format
    else:
      if format == 'AM':
        finalFormat = 'PM'
      else:
        finalFormat = 'AM'

    if (periodsOfTwelveHoursOverflow >= 2) or (periodsOfTwelveHoursOverflow == 1 and format == 'PM'):
      isNextdays = True


    suffix = ''
    daysCycled = 0
    if isNextdays:
      daysCycled = (totalHoursCopy // 12) / 2

      if daysCycled - int(daysCycled) == 0.5 and format == 'PM':
        daysCycled = daysCycled + 0.5
        
      
      if daysCycled == 1:
        suffix = ' (next day)'
      elif daysCycled > 1:
        suffix = ' (' + str(int(daysCycled)) + ' days later)'

    dayNameFuture = ''
    if starting_day is not False:
      for dayIndex, dayName in weekDays.items(): 
        if dayName.lower() == starting_day.lower():
          dayIndexSelected = dayIndex
      dayFutureIndex = dayIndexSelected + (daysCycled % 7)
      
      if dayFutureIndex > 7:
        dayFutureIndex = dayFutureIndex - 7

      dayNameFuture = ', ' + weekDays.get(dayFutureIndex)

    hoursString = str(totalHours)
    if hoursString == '0' and finalFormat == 'AM':
      hoursString = '12'
      
    minutesString = str(totalMinutes)

    if len(minutesString) == 1:
      minutesString = '0' + minutesString

    new_time = hoursString + ':' + minutesString + ' ' + finalFormat

    return new_time + dayNameFuture + suffix