# MFT-Detect-Response

Common framework for designing incident response and detections for common MFT
solutions.

This repo is has three main components:

-   MFTData – details the key software components of MFT solutions so that
    defenders can understand the underlying components of the MFT software. This
    information such as process names, file paths, ports, and services are
    critical for defenders to identify valuable incident response and detection
    data.

-   MFTDetect – scripts that leverage the MFTData to automatically generate
    detections for common threat detection and incident response tools.

-   MFTRespond – scripts and tools that can aide in responding to incidents
    involving a MFT server

-   MFTPlaybook – contains a MFT incident response playbook template that can be
    used as a starting point for incident responders to build incident response
    playbooks for MFT software. The template can be used in conjunction with a
    script to automatically pull the key MFT components from the MFTData and
    update the playbook template.
