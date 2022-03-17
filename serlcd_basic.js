module.exports = function(RED) {
    "use strict";
    const { spawn } = require('child_process');

    function SerLCDNode(config) {
        RED.nodes.createNode(this, config);
        let node = this;

        let child = spawn('python3', ['-u', __dirname + '/serlcd.py', config.size, config.address]);

        node.on('input', function(msg, send, done) {
            if (typeof(msg.payload === 'string')) {
                child.stdin.write(JSON.stringify({payload: msg.payload}) + '\n');
            }
            done();
        });

        node.on('close', function(removed, done) {
            child.stdin.write(JSON.stringify({payload: "clr:"}) + '\n');
            child.kill();
            done();
        });
    }
    RED.nodes.registerType("serlcd", SerLCDNode);
}
