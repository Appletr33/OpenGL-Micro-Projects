#version 300 es
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aColor;
layout (location = 2) in vec2 aTexCoord;

out mediump vec3 ourColor;
out mediump vec2 TexCoord;

uniform mediump mat4 model;
uniform mediump mat4 view;
uniform mediump mat4 projection;
uniform mediump vec3 hue;

void main()
{
    gl_Position = projection * view * model * vec4(aPos, 1.0);
    ourColor = aColor * hue;
    TexCoord = aTexCoord;
}