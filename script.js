function main() {
    let p = document.createElement('p')
    try {p.textContent = formatDate(CALENDAR[document.querySelector('input').value])}
    catch {p.textContent = '💀 date out of range 💀'}
    finally {document.querySelector('p').replaceWith(p)}
}

function formatDate(dateString) {
    [year, month, day] = dateString.split('-')
    month = MONTHS_NAMES[month]
    day = parseInt(day)
    return `${day}  ${month}  ${year}`
}

const MONTHS_NAMES = {
    "01" : "Muharram[1]",
    "02" : "Safar[2]",
    "03" : "Rabi' al-Awwal[3]",
    "04" : "Rabi' al-Thani[4]",
    "05" : "Jumada al-Ula[5]",
    "06" : "Jumada al-Akhirah[6]",
    "07" : "Rajab[7]",
    "08" : "Sha'ban[8]",
    "09" : "Ramadan[9]",
    "10" : "Shawwal[10]",
    "11" : "Dhu al-Qa'dah[11]",
    "12" : "Dhu al-Hijjah[12]"
}