// console.log("hello ")

const ReportBin = document.getElementById('report-btn')
const image = document.getElementById('img')
const modelbody = document.getElementById('model-body')

// console.log(image)
// console.log(ReportBin)

if (img) {
    ReportBin.classList.remove('set-not-visible')
}

ReportBin.addEventListener('click', ()=>{
    console.log('clicked')
    modelbody.append(image)
})