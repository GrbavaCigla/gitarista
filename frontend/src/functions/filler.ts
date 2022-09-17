export function changeFill(element: HTMLElement, color: string): number {
    let count = 1;

    for (let i = 0; i < element.children.length; i++) {
        element.children[i].setAttribute("fill", color);
        element.children[i].setAttribute("stroke", color);
        count += changeFill(element.children[i], color);
    }

    return count;
}