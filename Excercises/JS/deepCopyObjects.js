function isObject(subject) {
    return typeof subject == "object";
  }
  
function isArray(subject) {
    return Array.isArray(subject);
  }
  
function deepCopy(subject) {
    let copySubject;
  
    const subjectIsObject = isObject(subject);
    const subjectIsArray = isArray(subject);
  
    if (subjectIsArray) {
      copySubject = [];
    } else if (subjectIsObject) {
      copySubject = {};
    } else {
      return subject;
    }
  
    for (let key in subject) {
      const keyIsObject = isObject(subject[key]);
  
      if (keyIsObject) {
        copySubject[key] = deepCopy(subject[key]);
      } else {
        if (subjectIsArray) {
          copySubject.push(subject[key]);
        } else {
          copySubject[key] = subject[key];
        }
      }
    }
  
    return copySubject;
  }
  
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

Object.seal(exampleStudent)
console.log(delete exampleStudent.firstname)
console.log(exampleStudent.firstname)
console.log(Object.isSealed(exampleStudent))