import { createStudents } from "./FactoryPatternAndRORO.js";
import { deepCopy } from "./deepCopyObjects.js";

const studentTemplate = {
    firstname: undefined,
    lastname: undefined,
    email: undefined,
    age: undefined,
    approvedCourses: undefined,
    learningPaths: undefined,
    socialMedia: {
        facebook: undefined,
        instagram: undefined,
        linkedin: undefined,
        twitter: undefined,
    },
};

const exampleStudent = deepCopy(studentTemplate)
Object.defineProperty(exampleStudent, "firstname", {
    value: "Katerine Lopez",
    configurable: false,
})
console.log(exampleStudent)
Object.seal(exampleStudent)
console.log(exampleStudent.firstname)
console.log(Object.isSealed(exampleStudent))

createStudents('zorro')
