import { copyFile, mkdir, stat } from "node:fs/promises";
import { dirname, join } from "node:path";

const outputDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const source = new URL("./entry.png", import.meta.url);
const destination = join(outputDir, "entry.png");
const sourceInfo = await stat(source);
if (sourceInfo.size > 1048576) throw new Error("entry.png exceeds the 1 MiB gate");
await mkdir(dirname(destination), { recursive: true });
await copyFile(source, destination);
const writtenInfo = await stat(destination);
if (writtenInfo.size !== sourceInfo.size) throw new Error("output copy size mismatch");
