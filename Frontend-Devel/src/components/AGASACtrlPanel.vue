<template>
  <div class="container" :data-theme="theme">

    <!-- Common configuration shown first -->
    <div class="common-config-panel">
      <h4>Common Configuration</h4>
      <div class="config-grid">
        <label class="config-row">
          <span>Analog Output</span>
          <select v-model="commonConfig.output">
            <option :value="false">Off</option>
            <option :value="true">On</option>
          </select>
        </label>

        <label class="config-row">
          <span>ToT Polarity</span>
          <select v-model="commonConfig.polarity">
            <option value="normal">Normal</option>
            <option value="inverted">Inverted</option>
          </select>
        </label>

        <label class="config-row">
          <span>Inject Test Pulse</span>
          <select v-model="commonConfig.testpulse">
            <option :value="false">No</option>
            <option :value="true">Yes</option>
          </select>
        </label>

        <label class="config-row">
          <span>Comp. Threshold</span>
          <input type="number" v-model.number="commonConfig.threshold" min="-1.8" max="1.8" step="0.0035" />
        </label>

        <label class="config-row">
          <span>CSA Resistance</span>
          <select v-model="commonConfig.csa_res">
            <option :value="32">1 (32 kΩ)</option>
            <option :value="64">2 (64 kΩ)</option>
            <option :value="96">3 (96 kΩ)</option>
            <option :value="128">4 (128 kΩ)</option>
            <option :value="160">5 (160 kΩ)</option>
            <option :value="192">6 (192 kΩ)</option>
            <option :value="224">7 (224 kΩ)</option>
            <option :value="256">8 (256 kΩ)</option>
          </select>
        </label>

        <label class="config-row">
          <span>CSA Capacitance</span>
          <select v-model="commonConfig.csa_cap">
            <option :value="250">1 (250 fF)</option>
            <option :value="500">2 (500 fF)</option>
            <option :value="750">3 (750 fF)</option>
            <option :value="1000">4 (1000 fF)</option>
            <option :value="1250">5 (1250 fF)</option>
            <option :value="1500">6 (1500 fF)</option>
            <option :value="1750">7 (1750 fF)</option>
            <option :value="2000">8 (2000 fF)</option>
            <option :value="2250">9 (2250 fF)</option>
            <option :value="2500">10 (2500 fF)</option>
            <option :value="2750">11 (2750 fF)</option>
            <option :value="3000">12 (3000 fF)</option>
            <option :value="3250">13 (3250 fF)</option>
            <option :value="3500">14 (3500 fF)</option>
            <option :value="3750">15 (3750 fF)</option>
            <option :value="4000">16 (4000 fF)</option>
          </select>
        </label>

        <label class="config-row">
          <span>PZC Resistance</span>
          <select v-model="commonConfig.pzc_res">
            <option :value="32">1 (32 kΩ)</option>
            <option :value="64">2 (64 kΩ)</option>
            <option :value="96">3 (96 kΩ)</option>
            <option :value="128">4 (128 kΩ)</option>
            <option :value="160">5 (160 kΩ)</option>
            <option :value="192">6 (192 kΩ)</option>
            <option :value="224">7 (224 kΩ)</option>
            <option :value="256">8 (256 kΩ)</option>
          </select>
        </label>

        <label class="config-row">
          <span>PZC Capacitance</span>
          <select v-model="commonConfig.pzc_cap">
            <option :value="250">1 (250 fF)</option>
            <option :value="500">2 (500 fF)</option>
            <option :value="750">3 (750 fF)</option>
            <option :value="1000">4 (1000 fF)</option>
            <option :value="1250">5 (1250 fF)</option>
            <option :value="1500">6 (1500 fF)</option>
            <option :value="1750">7 (1750 fF)</option>
            <option :value="2000">8 (2000 fF)</option>
            <option :value="2250">9 (2250 fF)</option>
            <option :value="2500">10 (2500 fF)</option>
            <option :value="2750">11 (2750 fF)</option>
            <option :value="3000">12 (3000 fF)</option>
            <option :value="3250">13 (3250 fF)</option>
            <option :value="3500">14 (3500 fF)</option>
            <option :value="3750">15 (3750 fF)</option>
            <option :value="4000">16 (4000 fF)</option>
          </select>
        </label>

        <label class="config-row">
          <span>SHP Resistance</span>
          <select v-model="commonConfig.shp_res">
            <option :value="7.5">1 (7.5 kΩ)</option>
            <option :value="15">2 (15 kΩ)</option>
            <option :value="22.5">3 (22.5 kΩ)</option>
            <option :value="30">4 (30 kΩ)</option>
            <option :value="37.5">5 (37.5 kΩ)</option>
            <option :value="45">6 (45 kΩ)</option>
            <option :value="52.5">7 (52.5 kΩ)</option>
            <option :value="60">8 (60 kΩ)</option>
          </select>
        </label>

        <label class="config-row">
          <span>SHP Capacitance</span>
          <select v-model="commonConfig.shp_cap">
            <option :value="250">1 (250 fF)</option>
            <option :value="500">2 (500 fF)</option>
            <option :value="750">3 (750 fF)</option>
            <option :value="1000">4 (1000 fF)</option>
            <option :value="1250">5 (1250 fF)</option>
            <option :value="1500">6 (1500 fF)</option>
            <option :value="1750">7 (1750 fF)</option>
            <option :value="2000">8 (2000 fF)</option>
            <option :value="2250">9 (2250 fF)</option>
            <option :value="2500">10 (2500 fF)</option>
            <option :value="2750">11 (2750 fF)</option>
            <option :value="3000">12 (3000 fF)</option>
            <option :value="3250">13 (3250 fF)</option>
            <option :value="3500">14 (3500 fF)</option>
            <option :value="3750">15 (3750 fF)</option>
            <option :value="4000">16 (4000 fF)</option>
          </select>
        </label>
      </div>
      <button class="btn btn-primary" @click="applyCommonConfig">Apply to All Channels</button>
    </div>

    <!-- Sidebar: channel count, slide buttons and controls -->
    <div class="sidebar">
      <div class="sidebar-top">
        <h3>Channels</h3>
        <div class="theme-row">
          <label style="display:flex;align-items:center;gap:8px">
            <span style="font-size:13px;color:var(--muted)">Count</span>
            <select v-model.number="channelCount" style="padding:6px;border-radius:6px;border:1px solid var(--border);background:transparent;color:var(--text)">
              <option :value="16">16</option>
              <option :value="32">32</option>
              <option :value="64">64</option>
            </select>
          </label>

          <button class="btn btn-ghost" @click="toggleTheme">
            {{ theme === 'light' ? '🌤 Light' : '🌙 Dark' }}
          </button>
          <span class="badge">{{ selectedCount }} selected</span>
        </div>
      </div>

      <div class="channels-grid">
        <label v-for="ch in channels" :key="ch.id" class="ch-checkbox">
          <div class="switch">
            <input type="checkbox" v-model="ch.enabled" :id="'ch'+ch.id" />
            <span class="slider"></span>
          </div>
          <span class="ch-label">Ch. {{ ch.id }}</span>
        </label>
      </div>

      <div class="controls">
        <button class="btn" @click="enableAll">Enable All</button>
        <button class="btn" @click="disableAll">Disable All</button>
        <button class="btn btn-primary" @click="applyConfig">Apply Selected</button>
        <p class="status">Status: {{ status }}</p>
      </div>
    </div>

    <!-- Channel-specific panels shown after selector -->
    <div class="panels">
      <p v-if="!selected.length" class="muted">Select one or more channels to show settings</p>

      <div
        v-for="ch in selected"
        :key="ch.id"
        class="channel-panel"
      >
        <div class="panel-header">
          <h4>Channel {{ ch.id }}</h4>
        </div>

        <div class="panel-body">
          <hr class="full" />

          <div class="col">
            <label class="row">
              <span>Analog Output</span>
              <select v-model="ch.output">
                <option :value="false">Off</option>
                <option :value="true">On</option>
              </select>
            </label>

            <label class="row">
              <span>ToT Polarity</span>
              <select v-model="ch.polarity">
                <option value="normal">Normal</option>
                <option value="inverted">Inverted</option>
              </select>
            </label>

          <hr>

            <label class="row">
              <span>CSA Resistance</span>
              <select v-model="ch.csa_res">
                <option :value="32">1 (32 kΩ)</option>
                <option :value="64">2 (64 kΩ)</option>
                <option :value="96">3 (96 kΩ)</option>
                <option :value="128">4 (128 kΩ)</option>
                <option :value="160">5 (160 kΩ)</option>
                <option :value="192">6 (192 kΩ)</option>
                <option :value="224">7 (224 kΩ)</option>
                <option :value="256">8 (256 kΩ)</option>
              </select>
            </label>

            <label class="row">
              <span>PZC Resistance</span>
              <select v-model="ch.pzc_res">
                <option :value="32">1 (32 kΩ)</option>
                <option :value="64">2 (64 kΩ)</option>
                <option :value="96">3 (96 kΩ)</option>
                <option :value="128">4 (128 kΩ)</option>
                <option :value="160">5 (160 kΩ)</option>
                <option :value="192">6 (192 kΩ)</option>
                <option :value="224">7 (224 kΩ)</option>
                <option :value="256">8 (256 kΩ)</option>
              </select>
            </label>

            <label class="row">
              <span>SHP Resistance</span>
              <select v-model="ch.shp_res">
                <option :value="7.5">1 (7.5 kΩ)</option>
                <option :value="15">2 (15 kΩ)</option>
                <option :value="22.5">3 (22.5 kΩ)</option>
                <option :value="30">4 (30 kΩ)</option>
                <option :value="37.5">5 (37.5 kΩ)</option>
                <option :value="45">6 (45 kΩ)</option>
                <option :value="52.5">7 (52.5 kΩ)</option>
                <option :value="60">8 (60 kΩ)</option>
              </select>
            </label>

          </div>

          <div class="col">

            <label class="row">
              <span>Inject Test Pulse</span>
              <select v-model="ch.testpulse">
                <option :value="false">No</option>
                <option :value="true">Yes</option>
              </select>
            </label>

            <label class="row">
              <span>Comp. Threshold</span>
              <input type="number" v-model.number="ch.threshold" min="-1.8" max="1.8" step="0.0035" />
            </label>

          <hr>

            <label class="row">
              <span>CSA Capacitance</span>
              <select v-model="ch.csa_cap">
                <option :value="250">1 (250 fF)</option>
                <option :value="500">2 (500 fF)</option>
                <option :value="750">3 (750 fF)</option>
                <option :value="1000">4 (1000 fF)</option>
                <option :value="1250">5 (1250 fF)</option>
                <option :value="1500">6 (1500 fF)</option>
                <option :value="1750">7 (1750 fF)</option>
                <option :value="2000">8 (2000 fF)</option>
                <option :value="2250">9 (2250 fF)</option>
                <option :value="2500">10 (2500 fF)</option>
                <option :value="2750">11 (2750 fF)</option>
                <option :value="3000">12 (3000 fF)</option>
                <option :value="3250">13 (3250 fF)</option>
                <option :value="3500">14 (3500 fF)</option>
                <option :value="3750">15 (3750 fF)</option>
                <option :value="4000">16 (4000 fF)</option>
              </select>
            </label>

            <label class="row">
              <span>PZC Capacitance</span>
              <select v-model="ch.pzc_cap">
                <option :value="250">1 (250 fF)</option>
                <option :value="500">2 (500 fF)</option>
                <option :value="750">3 (750 fF)</option>
                <option :value="1000">4 (1000 fF)</option>
                <option :value="1250">5 (1250 fF)</option>
                <option :value="1500">6 (1500 fF)</option>
                <option :value="1750">7 (1750 fF)</option>
                <option :value="2000">8 (2000 fF)</option>
                <option :value="2250">9 (2250 fF)</option>
                <option :value="2500">10 (2500 fF)</option>
                <option :value="2750">11 (2750 fF)</option>
                <option :value="3000">12 (3000 fF)</option>
                <option :value="3250">13 (3250 fF)</option>
                <option :value="3500">14 (3500 fF)</option>
                <option :value="3750">15 (3750 fF)</option>
                <option :value="4000">16 (4000 fF)</option>
              </select>
            </label>

            <label class="row">
              <span>SHP Capacitance</span>
              <select v-model="ch.shp_cap">
                <option :value="250">1 (250 fF)</option>
                <option :value="500">2 (500 fF)</option>
                <option :value="750">3 (750 fF)</option>
                <option :value="1000">4 (1000 fF)</option>
                <option :value="1250">5 (1250 fF)</option>
                <option :value="1500">6 (1500 fF)</option>
                <option :value="1750">7 (1750 fF)</option>
                <option :value="2000">8 (2000 fF)</option>
                <option :value="2250">9 (2250 fF)</option>
                <option :value="2500">10 (2500 fF)</option>
                <option :value="2750">11 (2750 fF)</option>
                <option :value="3000">12 (3000 fF)</option>
                <option :value="3250">13 (3250 fF)</option>
                <option :value="3500">14 (3500 fF)</option>
                <option :value="3750">15 (3750 fF)</option>
                <option :value="4000">16 (4000 fF)</option>
              </select>
            </label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, computed, ref, watch } from 'vue'

const status = ref('idle')

// channel count selector and dynamic channels array
const channelCount = ref(16)
const channels = reactive([])

function createChannel(i) {
  // const isEven = (i + 1) % 2 === 0
  return {
    id: i + 1,
    enabled: false,
    output: false,
    polarity: 'normal',
    testpulse: false,
    threshold: 1.8,
    csa_res: 32,
    pzc_res: 32,
    shp_res: 7.5,
    csa_cap: 250,
    pzc_cap: 250,
    shp_cap: 250
  }
}

function initChannels(n) {
  const old = channels.slice()
  const next = Array.from({ length: n }, (_, i) => (old[i] ? old[i] : createChannel(i)))
  channels.splice(0, channels.length, ...next)
}

initChannels(channelCount.value)
watch(channelCount, (n) => {
  initChannels(n)
})

const selected = computed(() => channels.filter(c => c.enabled))
const selectedCount = computed(() => selected.value.length)

// common configuration for all channels
const commonConfig = reactive({
  output: false,
  polarity: 'normal',
  testpulse: false,
  threshold: 1.8,
  csa_res: 32,
  pzc_res: 32,
  shp_res: 7.5,
  csa_cap: 250,
  pzc_cap: 250,
  shp_cap: 250
})

// theme state
const theme = ref('light')
function toggleTheme() {
  theme.value = theme.value === 'light' ? 'dark' : 'light'
}

function enableAll() {
  channels.forEach(c => (c.enabled = true))
}
function disableAll() {
  channels.forEach(c => (c.enabled = false))
}

function applyCommonConfig() {
  channels.forEach(ch => {
    ch.output = commonConfig.output
    ch.polarity = commonConfig.polarity
    ch.testpulse = commonConfig.testpulse
    ch.threshold = commonConfig.threshold
    ch.csa_res = commonConfig.csa_res
    ch.pzc_res = commonConfig.pzc_res
    ch.shp_res = commonConfig.shp_res
    ch.csa_cap = commonConfig.csa_cap
    ch.pzc_cap = commonConfig.pzc_cap
    ch.shp_cap = commonConfig.shp_cap
  })
  status.value = `Applied common config to all ${channels.length} channels`
}

async function applyConfig() {
  status.value = 'Sending...'
  try {
    const payload = selected.value.map(c => ({
    id: c.id,
    output: c.output,
    polarity: c.polarity,
    testpulse: c.testpulse,
    threshold: c.threshold,
    csa_res: c.csa_res,
    pzc_res: c.pzc_res,
    shp_res: c.shp_res,
    csa_cap: c.csa_cap,
    pzc_cap: c.pzc_cap,
    shp_cap: c.shp_cap
    }))

    const res = await fetch('/api/channels/config', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ channels: payload })
    })

    if (!res.ok) {
      const text = await res.text()
      throw new Error(text || res.statusText)
    }

    const data = await res.json()
    status.value = data.message ?? `sent ${payload.length} channels`
  } catch (e) {
    status.value = 'error: ' + (e.message ?? e)
  }
}
</script>

<style scoped>
/* Theme variables */
.container {
  --bg: #ffffff;
  --panel: #fafafa;
  --muted: #6b7280;
  --text: #0f172a;
  --accent: #2563eb;
  --border: #e6e9ee;
  --shadow: 0 6px 18px rgba(16,24,40,0.06);
  background: var(--bg);
  color: var(--text);
  /* display: flex; */
  flex-direction: column;
  gap: 16px;
  padding: 16px;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  position: static;
  width: 100%;
  /* max-width: 1400px; */
  margin: 0 auto;
  box-sizing: border-box;
  overflow: visible;
  border-radius: 12px;
}

/* Dark theme overrides */
.container[data-theme="dark"] {
  --bg: #0b1220;
  --panel: #071228;
  --muted: #9aa4b2;
  --text: #e6eef8;
  --accent: #ea8d29ff;
  --border: rgba(255,255,255,0.06);
  --shadow: 0 8px 24px rgba(2,6,23,0.6);
}

/* Sidebar now spans full width at top */
.sidebar {
  width: 100%;
  border-right: none;
  border-bottom:1px solid var(--border);
  padding:12px;
  display:flex;
  flex-direction:column;
  gap:12px;
  flex-shrink: 0;
  margin-top: 10px;
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
  border-radius: 12px;
}

.sidebar h3 {
  font-weight: 700;
  font-size: 16px;
  margin: 0 0 12px 0;
  color: var(--accent);
}

.sidebar-top { display:flex; align-items:center; justify-content:space-between; gap:8px; }
.theme-row { display:flex; gap:8px; align-items:center; }

/* Buttons */
.btn {
  padding:8px 10px;
  border-radius:8px;
  background: transparent;
  border:1px solid var(--border);
  color: var(--text);
  cursor:pointer;
  transition: all .12s ease;
}
.btn:hover { transform: translateY(-2px); box-shadow: var(--shadow); }
.btn-primary {
  background: linear-gradient(90deg, var(--accent), color-mix(in srgb, var(--accent) 70%, black));
  color: white;
  border: none;
}
.btn-ghost { background: transparent; border: none; color: var(--muted); padding:4px 6px; }

/* Badge */
.badge {
  background: rgba(37,99,235,0.12);
  color: var(--accent);
  padding:4px 8px;
  font-size:12px;
  border-radius:999px;
}

/* Channel list (switch + label) - allow more columns now that it's wide */
.channels-grid {
  display:grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap:10px;
  margin-bottom:12px;
}
.ch-checkbox { display:flex; align-items:center; gap:10px; background:var(--panel); padding:6px 8px; border-radius:8px; border:1px solid var(--border); }

/* custom switch */
.switch { position: relative; width:44px; height:24px; }
.switch input { opacity:0; width:0; height:0; position:absolute; }
.slider {
  position:absolute;
  cursor:pointer;
  top:0; left:0; right:0; bottom:0;
  background: linear-gradient(180deg, rgba(0,0,0,0.03), rgba(0,0,0,0.01));
  border-radius: 999px;
  border:1px solid var(--border);
  transition: .18s;
}
.slider::before {
  content: "";
  position: absolute;
  height:18px; width:18px;
  left:3px; top:2px;
  background: white;
  border-radius:50%;
  box-shadow: 0 2px 6px rgba(2,6,23,0.12);
  transition: .18s;
}
.switch input:checked + .slider {
  background: linear-gradient(90deg, var(--accent), color-mix(in srgb, var(--accent) 65%, black));
  border-color: transparent;
}
.switch input:checked + .slider::before {
  transform: translateX(20px);
}

/* Channels label */
.ch-label {font-weight:600; color:var(--text); }

/* Controls */
.controls { display:flex; flex-direction:row; gap:8px; margin-top:8px; flex-wrap:wrap; }

/* Common config panel */
.common-config-panel {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 12px;
  margin-top: 8px;
  box-shadow: var(--shadow);
  flex-shrink: 0;
}
.common-config-panel h4 {
  font-weight: 700;
  font-size: 16px;
  margin: 0 0 12px 0;
  color: var(--accent);
}
.config-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 10px;
  margin-bottom: 12px;
}
.config-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  font-size: 13px;
}
.config-row select, .config-row input[type="number"] {
  width: 120px;
  padding: 6px;
  border-radius: 6px;
  border: 1px solid var(--border);
  background: transparent;
  color: var(--text);
  font-size: 13px;
}

/* Panels area - placed below sidebar and fills remaining height */
.panels {
  flex: 1 1 0;
  display:grid;
  gap:12px;
  padding:16px;
  overflow-y: auto;
  overflow-x: hidden;
  grid-template-columns: repeat(auto-fit, minmax(500px, 600px));
  align-content:start;
  width: 100%;
  min-height: 0;
}
.channel-panel {
  border:1px solid var(--border);
  padding:12px;
  border-radius:12px;
  background: var(--panel);
  box-shadow: var(--shadow);
  transition: transform .12s ease, box-shadow .12s ease;
}


.channel-panel:hover { transform: translateY(-6px); box-shadow: 0 20px 40px rgba(2,6,23,0.12); }

.panel-header { display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:8px;}
.panel-header h4 { font-weight:700; font-size:20px ; color:#ea8d29ff;}
.chip { background: rgba(0,0,0,0.06); padding:4px 8px; border-radius:999px; font-size:12px; color:var(--muted); }

/* Panel body layout */
.panel-body {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  align-items: start;
}
.panel-body .col { display:flex; flex-direction:column; gap:10px; }

/* make hr span both columns */
.panel-body .full {
  grid-column: 1 / -1;
  border: 0;
  height: 1px;
  background: var(--border);
  margin: 6px 0;
}

.row { display:flex; justify-content:space-between; align-items:center; gap:10px; margin:6px 0; }
.row input[type="number"], .row select, .row input[type="text"] { width:110px; padding:8px; border-radius:8px; border:1px solid var(--border); background: transparent; color:var(--text);   font-size: 13px;}

/* Muted text and status */
.muted { color:var(--muted); }
.status { font-size:13px; color:var(--muted); margin-top:8px; }

/* Responsive: keep the same stacked layout for small screens */
@media (max-width: 800px) {
  .panel-body { grid-template-columns: 1fr; }
  .controls { flex-direction:column; align-items:stretch; }
  .channels-grid { grid-template-columns: repeat(2, 1fr); }
  .panel-header h4 { font-size:18px; }
}
</style>