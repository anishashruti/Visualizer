console.log("hello ")

const ReportBin = document.getElementById('report-btn')
const image = document.getElementById('img')
const modelbody = document.getElementById('model-body')

const ReportName = document.getElementById('id_name')
const ReportRemark = document.getElementById('id_remark')
const csrf = document.getElementById('csrfmiddlewaretoken')
console.log(ReportName)
// console.log(image)
// console.log(ReportBin)

if (img) {
    ReportBin.classList.remove('set-not-visible')
}

ReportBin.addEventListener('click', ()=>{
    console.log('clicked')
    image.setAttribute('class','w-100')
    modelbody.prepend(image)
})