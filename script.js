const format = {
    '01' : 'Muharram[1]',
    '02' : '',
    '03' : '',
}


function main() {

    p = document.createElement('p')
    p.textContent = '💀 date out of range 💀'

    date = document.querySelector('input').value

    if (date in calendar) {
        let y, m, d = calendar[date].split('-')
        p.textContent = d + '  ' + format[m] + '  ' + y
    }

    document.querySelector('p').replaceWith(p)

}





function hijri_format(date) {
    let y, m, d = date.split('-')
    return d + '  ' +  formated_months[m] + '  ' + y
}