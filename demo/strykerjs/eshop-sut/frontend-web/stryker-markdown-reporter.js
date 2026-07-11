import fs from 'fs';
import path from 'path';
import { declareClassPlugin, PluginKind } from '@stryker-mutator/api/plugin';

const OUTPUT_FILE = 'strykerjs-report.md';

const STATUS_KEYS = ['Killed', 'Survived', 'Timeout', 'NoCoverage', 'Ignored', 'CompileError', 'RuntimeError'];

function emptyCounts() {
  return Object.fromEntries(STATUS_KEYS.map((k) => [k, 0]));
}

function scoreOf(counts) {
  const total = STATUS_KEYS.reduce((sum, k) => sum + counts[k], 0);
  const coveredDenominator = counts.Killed + counts.Survived + counts.Timeout;
  return {
    total,
    scoreTotal: total ? (counts.Killed / total) * 100 : 0,
    scoreCovered: coveredDenominator ? (counts.Killed / coveredDenominator) * 100 : 0,
  };
}

class MarkdownReporter {
  onMutationTestReportReady(report) {
    const fileEntries = Object.entries(report.files);
    const grandTotals = emptyCounts();
    const rows = [];
    const survivedByFile = [];
    const noCoverageByFile = [];

    for (const [file, data] of fileEntries) {
      const counts = emptyCounts();
      const survived = [];
      const noCoverage = [];

      for (const mutant of data.mutants) {
        if (counts[mutant.status] === undefined) continue;
        counts[mutant.status]++;
        grandTotals[mutant.status]++;
        if (mutant.status === 'Survived') survived.push(mutant);
        if (mutant.status === 'NoCoverage') noCoverage.push(mutant);
      }

      const { total, scoreTotal, scoreCovered } = scoreOf(counts);
      rows.push({ file, total, counts, scoreTotal, scoreCovered });
      if (survived.length) survivedByFile.push({ file, mutants: survived });
      if (noCoverage.length) noCoverageByFile.push({ file, mutants: noCoverage });
    }

    const grand = scoreOf(grandTotals);
    const lines = [];

    lines.push('# StrykerJS Mutation Report');
    lines.push('');
    lines.push(`_Generated: ${new Date().toISOString()}_`);
    lines.push('');
    lines.push('## Summary');
    lines.push('');
    lines.push('| File | Total | Killed | Survived | Timeout | No coverage | Score (total) | Score (covered) |');
    lines.push('|---|---|---|---|---|---|---|---|');
    for (const r of rows) {
      lines.push(
        `| ${r.file} | ${r.total} | ${r.counts.Killed} | ${r.counts.Survived} | ${r.counts.Timeout} | ${r.counts.NoCoverage} | ${r.scoreTotal.toFixed(2)}% | ${r.scoreCovered.toFixed(2)}% |`,
      );
    }
    lines.push(
      `| **All files** | **${grand.total}** | **${grandTotals.Killed}** | **${grandTotals.Survived}** | **${grandTotals.Timeout}** | **${grandTotals.NoCoverage}** | **${grand.scoreTotal.toFixed(2)}%** | **${grand.scoreCovered.toFixed(2)}%** |`,
    );
    lines.push('');

    lines.push('## Survived mutants');
    lines.push('');
    if (survivedByFile.length === 0) {
      lines.push('_No survived mutants._');
    } else {
      for (const { file, mutants } of survivedByFile) {
        lines.push(`### ${file}`);
        lines.push('');
        for (const m of mutants) {
          const replacement = (m.replacement ?? '').toString().replace(/\n/g, ' ').slice(0, 160);
          lines.push(`- line ${m.location.start.line} — **${m.mutatorName}**: \`${replacement}\``);
        }
        lines.push('');
      }
    }

    lines.push('## No-coverage mutants');
    lines.push('');
    if (noCoverageByFile.length === 0) {
      lines.push('_No uncovered mutants._');
    } else {
      for (const { file, mutants } of noCoverageByFile) {
        lines.push(`### ${file}`);
        lines.push('');
        for (const m of mutants) {
          const replacement = (m.replacement ?? '').toString().replace(/\n/g, ' ').slice(0, 160);
          lines.push(`- line ${m.location.start.line} — **${m.mutatorName}**: \`${replacement}\``);
        }
        lines.push('');
      }
    }

    const outPath = path.resolve(OUTPUT_FILE);
    fs.writeFileSync(outPath, lines.join('\n'));
    console.log(`[MarkdownReporter] wrote ${outPath}`);
  }
}

export const strykerPlugins = [declareClassPlugin(PluginKind.Reporter, 'markdown', MarkdownReporter)];
