// code stolen from OSMD demo
import * as jsPDF  from 'jspdf';
import * as svg2pdf from 'svg2pdf.js';
import { OpenSheetMusicDisplay, BackendType } from "opensheetmusicdisplay";

export async function savePDF(pdfName: string, sheet: OpenSheetMusicDisplay) {
    if (pdfName === undefined) {
        pdfName = sheet.sheet.FullNameString + ".pdf";
    }

    console.log(sheet);

    const backends = sheet.drawer.Backends;
    let svgElement = backends[0].getSvgElement();

    let pageWidth = 210;
    let pageHeight = 297;
    const engravingRulesPageFormat = sheet.rules.PageFormat;
    if (engravingRulesPageFormat && !engravingRulesPageFormat.IsUndefined) {
        pageWidth = engravingRulesPageFormat.width;
        pageHeight = engravingRulesPageFormat.height;
    } else {
        pageHeight = pageWidth * svgElement.clientHeight / svgElement.clientWidth;
    }

    const orientation = pageHeight > pageWidth ? "p" : "l";
    // create a new jsPDF instance
    const pdf = new jsPDF.jsPDF({
        orientation: orientation,
        unit: "mm",
        format: [pageWidth, pageHeight]
    });
    //const scale = pageWidth / svgElement.clientWidth;
    for (let idx = 0, len = backends.length; idx < len; ++idx) {
        if (idx > 0) {
            pdf.addPage();
        }
        svgElement = backends[idx].getSvgElement();

        if (!pdf.svg || !svg2pdf) {
            console.log("svg2pdf missing, necessary for jspdf.svg().");
            return;
        }

        await pdf.svg(svgElement, {
            x: 0,
            y: 0,
            width: pageWidth,
            height: pageHeight,
        })
    }

    pdf.save(pdfName); // save/download the created pdf
    //pdf.output("pdfobjectnewwindow", {filename: "osmd_createPDF.pdf"}); // open PDF in new tab/window

    // note that using jspdf with svg2pdf creates unnecessary console warnings "AcroForm-Classes are not populated into global-namespace..."
    // this will hopefully be fixed with a new jspdf release, see https://github.com/yWorks/jsPDF/pull/32
}