"use strict";

const CANVAS_SIZE = 80;
const GRID_SIZE = 8;
const CELL_SIZE = CANVAS_SIZE / GRID_SIZE;
const CANVAS_IDS = ["myCanvas", "myCanvas2", "myCanvas3", "myCanvas4"];
const OUTPUT_IDS = ["display", "display2", "display3", "display4"];

const canvases = [];

function InitThis() {
  CANVAS_IDS.forEach((id) => {
    const canvas = document.getElementById(id);
    if (!canvas) {
      return;
    }

    const context = canvas.getContext("2d");
    context.lineCap = "round";
    context.lineJoin = "round";

    const state = {
      canvas,
      context,
      isDrawing: false,
      lastX: 0,
      lastY: 0,
    };

    canvases.push(state);
    bindCanvasEvents(state);
    clearCanvas(state);
  });
}

function bindCanvasEvents(state) {
  const { canvas } = state;

  canvas.addEventListener("pointerdown", (event) => {
    event.preventDefault();
    const point = getCanvasPoint(canvas, event);
    state.isDrawing = true;
    state.lastX = point.x;
    state.lastY = point.y;
    canvas.setPointerCapture(event.pointerId);
  });

  canvas.addEventListener("pointermove", (event) => {
    if (!state.isDrawing) {
      return;
    }

    event.preventDefault();
    const point = getCanvasPoint(canvas, event);
    drawLine(state, point.x, point.y);
  });

  ["pointerup", "pointercancel", "pointerleave"].forEach((eventName) => {
    canvas.addEventListener(eventName, () => {
      state.isDrawing = false;
    });
  });
}

function getCanvasPoint(canvas, event) {
  const rect = canvas.getBoundingClientRect();
  return {
    x: ((event.clientX - rect.left) / rect.width) * canvas.width,
    y: ((event.clientY - rect.top) / rect.height) * canvas.height,
  };
}

function drawLine(state, x, y) {
  const { context } = state;
  const colorInput = document.getElementById("selColor");
  const widthInput = document.getElementById("selWidth");

  context.strokeStyle = colorInput ? colorInput.value : "#141c3a";
  context.lineWidth = widthInput ? Number(widthInput.value) : 14;
  context.beginPath();
  context.moveTo(state.lastX, state.lastY);
  context.lineTo(x, y);
  context.stroke();

  state.lastX = x;
  state.lastY = y;
}

function clearCanvas(state) {
  const { canvas, context } = state;
  context.setTransform(1, 0, 0, 1, 0, 0);
  context.clearRect(0, 0, canvas.width, canvas.height);
  context.fillStyle = "#ffffff";
  context.fillRect(0, 0, canvas.width, canvas.height);
}

function clearArea() {
  canvases.forEach(clearCanvas);
  ["opening_bracket", ...OUTPUT_IDS, "closing_bracket"].forEach((id) => {
    const element = document.getElementById(id);
    if (element) {
      element.textContent = "";
    }
  });
}

function getCompressedImage(context) {
  const imageData = context.getImageData(0, 0, CANVAS_SIZE, CANVAS_SIZE).data;
  const cells = Array.from({ length: GRID_SIZE * GRID_SIZE }, () => []);

  for (let y = 0; y < CANVAS_SIZE; y += 1) {
    for (let x = 0; x < CANVAS_SIZE; x += 1) {
      const pixelIndex = (y * CANVAS_SIZE + x) * 4;
      const red = imageData[pixelIndex];
      const green = imageData[pixelIndex + 1];
      const blue = imageData[pixelIndex + 2];
      const alpha = imageData[pixelIndex + 3] / 255;
      const brightness = (red + green + blue) / 3;

      const inkStrength = alpha * (255 - brightness);
      const cellIndex = Math.floor(y / CELL_SIZE) * GRID_SIZE + Math.floor(x / CELL_SIZE);
      cells[cellIndex].push(inkStrength);
    }
  }

  return cells.map((cell) => {
    const total = cell.reduce((sum, value) => sum + value, 0);
    const average = total / cell.length;
    return ((average / 255) * 16).toFixed(2);
  });
}

function array() {
  const opening = document.getElementById("opening_bracket");
  const closing = document.getElementById("closing_bracket");

  if (opening) {
    opening.textContent = "[";
  }

  canvases.forEach((state, index) => {
    const element = document.getElementById(OUTPUT_IDS[index]);
    if (!element) {
      return;
    }

    const values = getCompressedImage(state.context);
    const suffix = index === canvases.length - 1 ? "" : ",";
    element.textContent = `[${values.join(",")}]${suffix}`;
  });

  if (closing) {
    closing.textContent = "]";
  }
}
